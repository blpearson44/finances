from datetime import timedelta, date
import json


class Account:
    def __init__(self, name="Default", accountType="Default", date=date(1, 1, 1), balance=0):
        self.name = name
        self.accountType = accountType
        self.date = date
        self.balance = balance
        # self.age = date.today() - date

    def getAge(self):
        return date.today() - self.date

    def printInfo(self):
        print("Account:\t " + str(self.name))
        print("Type:\t\t " + str(self.accountType))
        print("Date Created:\t", self.date.strftime("%m/%d/%Y"))
        print("Age:\t\t", int(self.getAge().total_seconds()/3600/24/365),
              "years", int(self.getAge().total_seconds()/3600/24 % 365), "days")
        print("Balance:\t " + str(self.balance))

    def loadInfo(self, info):
        self.name = info['name']
        self.accountType = info['accountType']
        self.date = info['date']
        self.balance = info['balance']
        #self.age = date.today() - info['date']


def transform(object):
    if isinstance(object, Account):
        return object.__dict__
    if isinstance(object, date):
        return (object.day, object.month, object.year)
    else:
        raise TypeError("Only Index and Account can be serialized.")


wf = Account("Wells Fargo", "Checking", date(2012, 8, 20), 1000)
with open("data1.json", "w") as f:
    json.dump(wf, f, default=transform)

# with open("data1.json", "r") as f:
#     data = json.load(f)

# print(data)
# a1 = Account()
# a1.loadInfo(data)
# a1.printInfo()
