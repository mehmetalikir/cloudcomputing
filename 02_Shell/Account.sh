#!/usr/bin/env bash
# Author: Mehmet A. Kir

echo "Please Enter Your Name: "
read USER
echo "Hi $USER, Please Enter Your ID:"
#read $ID
echo "Please Enter Your PIN: "
#read $PIN
ID="ABC999"
PIN=111
COUNTER=0
while [[ $COUNTER -le 3 ]]; do
  COUNTER=$((COUNTER + 1))
  if [[ $ID == ABC999 ]] && [[ $PIN -eq 111 ]]; then
    echo "Welcome.."
    BALANCE=1000
    DEPOSIT=0
    WITHDRAW=0
    printf "%s\n" "1: balance" "2: deposit" "3: withdraw" "4: exit"
    read MENU
    case $MENU in
    1)
      echo "Your Balance : $BALANCE"
      ;;
    2)
      echo "Please Enter Amount to Deposit: "
      read AMOUNT
      BALANCE=$((BALANCE + $AMOUNT))
      echo "Your Balance : $BALANCE"
      ;;
    3)
      echo "Please Enter Amount to Withdraw: "
      read AMOUNT
      BALANCE=$((BALANCE - $AMOUNT))
      echo "Your Balance : $BALANCE"
      ;;
    4)
      exit 1
      ;;
    esac
  else
    echo "Please Enter Your ID: (your $COUNTER attempt)"
    read
    echo "Please Enter Your PIN:"
    continue
  fi
done
