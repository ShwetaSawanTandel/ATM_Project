balance=20000
uname='alice'
bal=''
mobile_no=''
pin=1234


def chebal():
    global pin
    global balance
    global uname
    
    ename=input('Enter name:')
    epin=int(input('Enter pin:'))
    if ename==uname and pin==epin:
        print('your current balance is:', balance)
    else:
        print('Invallid credentials')
        

def withdraw():
    global pin
    global balance
    epin=int(input('Enter pin:'))
    if epin==pin:
        wamt=int(input('Enter amount to withdraw:'))
        balance=balance-wamt
        display_bal=input('you want to print balanceenter yes/no:')
        if display_bal=='yes':
            print(balance)
        else:
            print('Thank you')
    else:
        print('Password is incorrect Try again')



def deposit():
    global pin
    global balance
    epin=int(input('Enter pin:'))
    if epin==pin:
        damt=int(input('Enter amount to deposit:'))
        balance=balance+damt
        display_bal=input('you want to print balance enter yes/no:')
        if display_bal=='yes':
            print(balance)
        else:
            print('Thank you')
    else:
        print('Password is incorrect Try again')



def cpin():
    global pin
    epin=int(input('Enter pin:'))
    if epin==pin:
        npin=int(input('Enter new pin:'))
        pin=npin
    else:
        print('Password is incorrect Try again')

def add_user():
    global balance
    global uname
    global bal
    global mobile_no
    global pin
    f=open('atmdata.txt', 'a')
    nuname = input('Enter name: ')
    uname=nuname
    balance = int(input('Enter balance: '))
    while True:
        mobile_no = input('Enter Mobile number: ')
        if len(mobile_no) == 10:
            break
        else:
            print('mobile number should be 10 digit ')
    pin = int(input('Enter PIN: '))
    
    user_data = f"{uname},{balance},{mobile_no},{pin}\n"
        
    f.write(user_data)
    f=open('atmdata.txt','r')
    
    a=f.read()

    
    
while True:
    print('*****************WELCOME TO SBI ATM*******************')
    print('1.Check Balance')
    print('2.Debit(Withdraw)')
    print('3.Credit(Deposit)')
    print('4.Change Pin')
    print('5.Add user')
    print('6.Exit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        chebal()
    elif choice==2:
        withdraw()
    elif choice==3:
        deposit()
    elif choice==4:
        cpin()
    elif choice==5:
        add_user()
    elif choice==6:
        print('Thank you')
        break
    else:
        print('Wrong Choice')





    






