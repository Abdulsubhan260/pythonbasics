class Account:
    def __init__(self,username,pin,balance):
        self.username=username
        self.pin=pin
        self.balance=balance
    def check_pin(self):
        pin=int(input("enter your pin: "))
        return pin==self.pin
        # if pin==self.pin:
        #     print("correct pin entered")
        # else:
            # print("incorrect pin.access denied!")
    def deposit(self,amount):
        # self.check_pin()
        if not self.check_pin():
            print("incorrect pin")
            return

        if amount<=0:
            print("invalid amount")
        else:
            self.balance+=amount
            print("amount deposited.your current account balance is",self.balance)
    def withdraw(self,amount):

        # self.check_pin()
        if not self.check_pin():
            print("access denied")
            return
            
        if amount<=0:
            print("invalid amount!")
        elif amount>0:
         self.balance-=amount
         print(f"{amount} is withdrawn.current balance is {self.balance}")

        # return self.balance
        
    def run(self):
        self.check_pin()
        while True:
            print("press 1 for deposit")
            print("press 2 for withdraw")
            print("press 3 for exit")
            choice=input("enter your choice: ")
            if choice=='1':
                money=int(input("enter amount: "))
                self.deposit(money)
            elif choice=='2':
                money=int(input("enter amount: "))
                self.withdraw(money)
            elif choice=='3':
                print("thank you for using..")
                break
            else:
                print("invalid choice.enter valid choice.")
user1=Account("ali",1234,5000)
user1.run()
