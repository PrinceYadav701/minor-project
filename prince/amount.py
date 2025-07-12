print("\t\t\t\t\t\t welcome to punjab national bank")
import bank_balance
pin=1234
if "card"==input("enter your card"):
    print("welcome")
    if pin==int(input("enter your pin")):
     print('\t\t\t\t\t\t1)check balance\n\t\t\t\t\t\t2)cash withdrawn')
    option=int(input("select your option"))
    if option==1:
         print("your account balance is =",bank_balance.amount)
    elif option==2:
        user_amt=int(input("enter amount"))
        bank_balance=bank_balance.amount-user_amt
        file=open('bank_balance.py','w')
        file.write(f'amount={bank_balance}')
        file.close()  
    else:
        print("invalid pin")
else:
    print("invalid card")