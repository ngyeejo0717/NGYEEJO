import pandas as pd
import os

def verify_user(ic, password):
    if len(ic) != 12 or not ic.isdigit():
        return False
    return password == ic[-4:]

def calculate_tax(income, tax_relief):
    chargeable = income - tax_relief
    if chargeable <= 0:
        return 0

    tax = 0
    brackets = [(5000, 0.00),(15000, 0.01),(15000, 0.03),(15000, 0.08),(20000, 0.14),(30000, 0.21)]
    remaining = chargeable
    for amount, rate in brackets:
        if remaining > amount:
            tax += amount * rate
            remaining -= amount
        else:
            tax += remaining * rate
            return round(tax, 2)
    tax += remaining * 0.24
    return round(tax, 2)

def save_to_csv(data, userfile):
    df = pd.DataFrame([data])
    if not os.path.exists(userfile):
        df.to_csv(userfile, index=False)
    else:
        df.to_csv(userfile, index=False, mode='a', header=False)

def read_from_csv(userfile):
    if not os.path.exists(userfile):
        return None
    return pd.read_csv(userfile)