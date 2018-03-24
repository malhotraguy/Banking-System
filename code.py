from abc import ABCMeta,abstractmethod
from random import randint
class Account(metaclass = ABCMeta):
    @abstractmethod
    def createSavingAcc(self,name,initialDeposit):
        return 0
    def authenticate(self,name,AccNumber):
        return 0
    def withdraw(self,withdrawalAmount):
        return 0
    def deposit(self,depositAmount):
        return 0
    def displayBalance(self):
        return 0

class SavingAccount(Account):
    def __init__(self):
        self.savingAccounts={}
    def createSavingAcc(self,name,initialDeposit):
        self.AccNumber=randint(10000,99999)
        self.savingAccounts[self.AccNumber]=[name,initialDeposit]
        print("Your Account No. is : ",self.AccNumber)
        print()
    def authenticate(self,name,AccNumber):
        if AccNumber in self.savingAccounts.keys():
            if self.savingAccounts[AccNumber][0]==name:
                print("Authentication Successful")
                print()
                self.name=name
                self.AccNumber=AccNumber
                return True
            else:
                print("Authentication Failed")
                print()
                return False
        else:
            print("Authentication Failed")
            print()
            return False
    def withdraw(self,withdrawalAmount):
        if (self.savingAccounts[self.AccNumber][1]-withdrawalAmount)>0:
            self.savingAccounts[self.AccNumber][1] -=withdrawalAmount
            print("Amount=CAD$",withdrawalAmount,"has been withdrawn")
            print()
            SavingAccount.displayBalance(self)
        else:
            print("Insufficient Balance!:You can't withdraw more than your balance")
            print()

    def deposit(self,depositAmount):
        self.savingAccounts[self.AccNumber][1]+= depositAmount
        print("Amount=CAD$",depositAmount,"has been deposited to your Account")
        print()
        SavingAccount.displayBalance(self)
    def displayBalance(self):
        return print("Balance of ",self.savingAccounts[self.AccNumber][0],"with Account Number=",self.AccNumber,"is CAD$",self.savingAccounts[self.AccNumber][1])
savingaccount=SavingAccount()
while True:
    print()
    print("Press 1 to open a new account")
    print("Press 2 to access your account")
    print("Press 3 to exit!!")
    userChoice = input()
    if userChoice == "1":
        name = input("Enter Your Full Name: ").capitalize()
        initialDeposit = int(input("Enter the amount you want to deposit CAD$="))
        savingaccount.createSavingAcc(name, initialDeposit)
        savingaccount.displayBalance()
    elif userChoice == "2":
        name = input("Enter Your Full Name: ").capitalize()
        AccNumber = int(input("Enter your Account Number: "))
        auth = savingaccount.authenticate(name, AccNumber)
        if auth==True:
            while True:
                print("Press 1 to withdraw")
                print("Press 2 to  deposit")
                print("Press 3 to display balance")
                print("Press 4 to go to previous menu")
                userChoice = int(input())
                if userChoice == 1:
                    withdrawalAmount = int(input("Enter the amount you want to withdraw:CAD$ "))
                    savingaccount.withdraw(withdrawalAmount)
                elif userChoice == 2:
                    depositAmount = int(input("Enter the amount you want to deposit:CAD$ "))
                    savingaccount.deposit(depositAmount)
                elif userChoice == 3:
                    savingaccount.displayBalance()
                elif userChoice == 4:
                    break
                else:
                    print("Invalid User Choice")


    elif userChoice == "3":
        quit()
    else:
        print("Invalid User Choice")

