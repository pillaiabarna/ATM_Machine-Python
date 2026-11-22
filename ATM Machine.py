print('------------------ATM Machine------------------')
balance = int(input("Enter your Balance Amount:"))
while True: 
    print("1. Check your Balance:")
    print("2. Deposit your Money:")
    print("3. Withdraw your Money:")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
           print ("Your balance amount is:", balance)
    elif choice == 2:
           deposit = int(input("Enter the amount that you want to deposit:"))
           balance =  balance+deposit
           print("Your new balance amount is:", balance)
    elif choice == 3:
           withdraw =  int(input("Enter the amount that you want to withdraw:"))
           if withdraw > balance:
                         print("Insufficient balance")
           else:
            balance = balance - withdraw
            print("Your new balance amount is:", balance)
    elif choice == 4:
            print("Thank your for using our ATM Machine.")
            break
    print('------------------End of your Transaction------------------')