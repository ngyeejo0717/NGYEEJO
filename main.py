from functions import verify_user, calculate_tax, save_to_csv, read_from_csv

userfile = "tax_records.csv"
registered_users = {}

while True:
    print("=== Malaysian Tax Input System ===")
    print("1. Register User")
    print("2. Login & Calculate Tax")
    print("3. View Tax Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = input("Enter IC Number (12 digits): ")
        ic = user_id
        password = ic[-4:]

        if len(ic) != 12 or not ic.isdigit():
            print("Invalid IC number! Must be 12 digits.")
            continue

        registered_users[user_id] = ic
        print("Registration successful!")
        print("Your password is", password)
        
    elif choice == "2":
        user_id = input("Enter yout ic: ")

        if user_id not in registered_users:
            print("User not registered!")
            continue

        ic = registered_users[user_id]
        password = input("Enter your password: ")

        if not verify_user(ic, password):
            print("Wrong password!")
            continue

        print("Login successful!")
        
        income = float(input("Enter annual income (RM): "))
        relief = float(input("Enter tax relief amount (RM): "))

        tax_payable = calculate_tax(income, relief)

        print(f"\nYour tax payable is: RM {tax_payable:.2f}")

        data = {
            "IC": ic,
            "Income": income,
            "Tax Relief": relief,
            "Tax Payable": tax_payable
        }

        save_to_csv(data, userfile)
        print("Data saved to CSV!")

    elif choice == "3":
        df = read_from_csv(userfile)
        if df is None:
            print("No tax records found!")
        else:
            print("=== TAX RECORDS ===")
            print(df)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")