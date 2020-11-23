from datetime import timedelta, date


class Account:
    def __init__(self, name, accountType, date, balance):
        self.name = name
        self.accountType = accountType
        self.date = date
        self.balance = balance
        self.age = date.today() - date

    def printInfo(self):
        print("Account:\t " + str(self.name))
        print("Type:\t\t " + str(self.accountType))
        print("Date Created:\t", self.date.strftime("%m/%d/%Y"))
        print("Age:\t\t", int(self.age.total_seconds()/3600/24/365),
              "years", int(self.age.total_seconds()/3600/24 % 365), "days")
        print("Balance:\t " + str(self.balance))


wf = Account("Wells Fargo", "Checking", date(2012, 8, 20), 1000)
wf.printInfo()
