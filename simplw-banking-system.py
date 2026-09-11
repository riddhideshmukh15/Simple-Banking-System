name = input("Enter your name: ")

pin = input("Create your PIN: ")

balance = 0

print("\nAccount created successfully!")
print("Welcome,", name)

while True:
    print("\n==== BANKING SYSTEM ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("Your balance is:", balance)
        else:
            print("Incorrect PIN.")

    elif choice == "2":
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print(amount, "deposited successfully.")
                print("New balance:", balance)
            else:
                print("Please enter a valid amount.")
        else:
            print("Incorrect PIN.")

    elif choice == "3":
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Please enter a valid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(amount, "withdrawn successfully.")
                print("Remaining balance:", balance)
        else:
            print("Incorrect PIN.")

    elif choice == "4":
        print("Thank you,", name, "for using our Banking System!")
        break

    else:
        print("Invalid choice. Please try again.")