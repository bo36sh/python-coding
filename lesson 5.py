print("hello world")

class bankaccount(object):
    #init class
    def __init__(self,name,acc_num,sort_code,balance):
        self.name = name
        self.acc_num = acc_num
        self.sort_code = sort_code
        self.balance = balance
     #deposit method
    def deposit(self,amt):
        print("the current balance is",self.balance)
        print("i have deposited {} in mu account".format(amt))
        self.balance = self.balance + amt
        print("my new account balance is", self.balance)

    def withdraw(self,amt):
        if self.balance < 0:
            print("insufficient balance")
            print("add credits to withdraw")
        print("the current balance is", self.balance)
        print("iam withdrawing {} from my acc", format(amt))
        self.balance = self.balance - amt
        print("my new balance ",self.balance)
    def getbalance(self):
        print("checking my balance", self.balance)
    def info(self):
        print("the account holder is" ,self.name)
        print("their acc numm {} and sort code {}".format(self.acc_num,self.sort_code))
        print("the account balnce is:" ,self.balance)
    def creatATM(self):
        print("card number:1234 5678 9101 2131")
        print("EXP MM{} YYYY{}".format(10,2030))
        print("CVV 345")
        print("NAME",self.name)
    def regaddress(self,addr):
        print("current address is:", addr)
    def phonenumber(self,NUM):
        print("my phone number is",NUM)





u1 = bankaccount("john doe",123456,"01-01-01",0)
print("=========runing acc deposit=======")
u1.deposit(50)
print("======runing te debit function======")
u1.withdraw(20)
print("=======runing the balance============")
u1.getbalance()
print("============info method========")
u1.info()
print("=======creating ATM card=========")
u1.creatATM()
print("=====register address=======")
u1.regaddress("1 travelyn square leeds ls1 1cx")
print("===your phone number==")
u1.phonenumber(11223344)


print("==building a pormot for the bank account")
name = input("enter your name:")
acc_num = input("enter your account number:")
sort_code = input("enter your sort code:")
balance = int(input("enter your balance"))
u2 = bankaccount(name,acc_num,sort_code,balance)

while True:
    print("\n =====bank menu=====")
    print("1.deposit")
    print("2.ithdraw")
    print("3.check balance")
    print("4.account info")
    print("5.creat ATM card")
    print("6.register address")
    print("7.register phone number")
    print("8.exit")

    choice = input(("choose an option (1-8):"))
    if choice == "1":
        amount =int(input("enter deposit amount:£"))
        u2.deposit(amount)
    elif choice == "2":
        amount = int(input("enter withdraw amount:£"))
        u2.withdraw(amount)
    elif choice == "3":
        u2.getbalance()
    elif choice == "4":
        u2.info()
    elif choice == "5":
        u2.creatATM()
    elif choice == "6":
        phone == input("enter your phone number")
        u2.phonenumber(phone)
    elif choice == "7":
        addr = input("enter your address")
        u2.regaddress(addr)
    else:
        print("choose between options above")
        exit()