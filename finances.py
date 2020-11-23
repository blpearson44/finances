from datetime import date

class Account:
    def __init__(self, name, accountType, date, balance):
        self.name = name
        self.accountType = accountType
        self.date = date
        self.balance = balance
    
    def printInfo(self):
        print("Account:\t" + str(self.name))
        print("Type:\t\t" + str(self.accountType))
        print("Date created:\t" + str(self.date))
        print("Balance:\t" + str(self.balance))

a1 = Account("Wells Fargo", "Checking", date.today(), 1000)
a1.printInfo()
