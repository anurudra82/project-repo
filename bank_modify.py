
import sys
class customer:
    bankname="Anurudra's bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def openacount(self,first_name,last_name,mobile_no,Adhar_no):
    
        print('welcome',first_name,last_name)
        print('your given mobile number is:',mobile_no)
        print('your given Adhar number is:',Adhar_no)
        print('THANK YOU,your Account successfully Opened')
        print()
    
    
    def deposite(self,amount):
        self.balance=self.balance+amount
        print('your amount after deposite:',self.balance)
    
    def withdraw(self,amount):
        if amount > self.balance:
            print('insufficient balance...........')
            sys.exit()
            
        self.balance=self.balance-amount
        print('your amount after withdraw:',self.balance)

print('Welcome to',customer.bankname)
name=input('Enter the your name in register: ')
c=customer(name)

while True:

    print('O->Open account:\nD->DEPOSITE:\nW->WITHDRAW:\nE->EXIT')
    option=input('Plese choose your option: ')


    if option== 'o' or option== 'O':
        first_name=input('Enter your first name: ')
        last_name=input('Enter your last name:  ')
        mobile_no=int(input('Enter your mobile number: '))
        Adhar_no=int(input('Enter your Adhar number: '))
        c.openacount(first_name,last_name,mobile_no,Adhar_no)
        print()

    elif option=='d' or option=='D':
        amount=float(input('Enter the amount:'))
        c.deposite(amount)
        print()

    elif option=='W' or option=='w':
        amount=float(input('Enter the amount:'))
        c.withdraw(amount)
        print()
        
    elif option=='e'or option=='E':
        print('Thanks for using our bank have a nice day')
        sys.exit()
    else:
        print('Invelid option plzzz choose valid option')   
        
        
        

    