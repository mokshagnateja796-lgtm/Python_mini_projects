## This is my first Python mini project uploaded to GitHub //
balance = 5000

while True:
    print("ATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter the Choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        money = int(input("Enter the money: "))
        balance = balance + money
        print("Your money is Deposited")
        print("Current Balance:", balance)

    elif choice == 3:
        money = int(input("Enter the money: "))

        if money <= balance:
            balance = balance - money
            print("Your amount Withdraw done")
            print("Current Balance:", balance)
        else:
            print("Insufficient amount")

    elif choice == 4:
        print("Thank You")
        break

else:
 print("Invalid Choice")