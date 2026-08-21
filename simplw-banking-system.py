balance=0
while True:
    print("\n====BANKING SYSTEM====")
    print("1. check balance")
    print("2. Deposite money")
    print("3.Withdraw money")
    print("4.Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        print("Your balance is:",balance)
    elif choice=="2":
        amount=float(input("Enter amount to deposite:"))
        if amount>0:
            balance+=amount
            print("",amount,"deposited successfully.")
            print("New balance:",balance)
        else:
            print("Please enter a valid amount.")
    elif choice=="3":
        amount=float(input("Enter amount to withdraw:"))
        if amount<=0:
            print("Please enter a valid amount.")
        elif amount>balance:
            print("Insufficient balance.")
        else:
            balance-=amount
            print("",amount,"withdraw sucessfully.")
            print("Remaining balance:",balance)
    elif choice=="4":
        print("Thank you for using our Banking System!")
        break
    else:
        print("Invalid choice.please try again.")