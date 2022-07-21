#!/usr/bin/env python3.8
# Author: Mehmet A. Kir
# Email : @


ID = int(input("Please enter your ID:"))
PIN = int(input("Please enter your PIN:"))

while True:
    if ID == 999 and PIN == 000:
        balance = 1000
        deposit = 0
        withdraw = 0
        while True:
            print(f"\n", "--Main Menu--\n1.balance\n2.deposit\n3.withdraw\n4.exit")
            menu = int(input("Enter a choice:  "))
            if menu == 1:
                print(f"Your Balance: ${balance}")
            elif menu == 2:
                amount = int(input("Pls Enter Amount to Deposit:"))
                balance += amount
                print(f"Your Balance: ${balance}")
            elif menu == 3:
                amount = int(input("Pls Enter Amount to Withdraw:"))
                balance -= amount
                print(f"Your Balance: ${balance}")
            else:
                exit(0)

    else:
        print("Please Call Your Branch!!")
        break







