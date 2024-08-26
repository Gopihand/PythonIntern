import time
print("please insert your Card")
time.sleep(5)
password=2108
pin=int(input("Enter your PIN : "))
balance=5000
if pin==password:
    while True:
        print("""
              1==balance
              2==withdraw balance
              3==deposit balance
              4==exit
              """
              )
        try:
            option=int(input("Please enter your choice"))
        except:
                print("Please enter valid option")
        if option==1:
          print(f"your current balance is {balance}")
        if option==2:
              withdraw_amount=int(input("Please enter withdraw amount:  "))
              balance=balance-withdraw_amount
              print(f"{withdraw_amount} is debited from your account")
              print(f"your current balance {balance}")
        if option==3:
            deposit_amount=int(input("Please enter deposit_amount:  "))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your current balance is {balance}")
        if option==4:
            break
    
else:
    print("Wrong pin Please try again")
            
    