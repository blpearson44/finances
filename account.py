from datetime import timedelta, date


class Account:
    def __init__(self, name="Default", accountType="Default", date=date(1, 1, 1), balance=0):
        self.name = name
        self.accountType = accountType
        self.date = date
        self.balance = balance

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
        self.date = date(info['date'][0], info['date'][1], info['date'][2])
        self.balance = info['balance']


def transform(object):
    if isinstance(object, Account):
        return object.__dict__
    if isinstance(object, date):
        return (object.year, object.month, object.day)
    else:
        raise TypeError("Only Index and Account can be serialized.")
