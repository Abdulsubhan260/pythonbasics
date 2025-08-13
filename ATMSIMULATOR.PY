class useraccount:
    def __init__(self,username,pin,balance):
        self.username=username
        self.pin=pin
        self.balance=balance
    def check_pin(self,pin):
        return pin==self.pin
    def withdraw(self,amount):
        if amount<=self.balance:
           self.balance-=amount
           print(f'{amount} withdrwan.remaining balance is: {self.balance}')
        else:
             print("insufficent balance")

    def check_balance(self):
        print(f'current balance is: {self.balance}')
class atm:
    def __init__(self,account):
        self.account=account
    def run(self):
        print("**welcome to ATM simulator**")
        entered_pin=input("enter your PIN: ")
        if not self.account.check_pin(entered_pin):
            print("Invalid PIN. Access denied.") 
            return
        while True:
            print("press 1 for withdraw")
            print("press 2 for check_balance")
            print("press 3 for exit ")
            choice=input("enter your choice: ")
            if choice=='1':
                amount = int(input("Enter amount to withdraw: "))
                self.account.withdraw(amount)
            elif choice=='2':
                self.account.check_balance()  
            elif choice=='3':1234

            print("Thank you for using.....")
            break

user1 = useraccount("Ali", "1234", 5000)
atm_machine = atm(user1)
atm_machine.run()
