# playing with how to convert the dates from csv into the python date format
# I think it is probably just going to be equal to the delta of some date in the
# past and a current date
class Transaction:
    def __init__(self, account=None, date=None, amount=None, category=None):
        self.account = account
        self.date = date
        self.amount = amount
        self.category = category

    def printInfo(self):
        print(self.account + "\t" + str(self.date) + "\t" +
              str(self.amount) + "\t" + self.category)
