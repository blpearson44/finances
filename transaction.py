# playing with how to convert the dates from csv into the python date format
# I think it is probably just going to be equal to the delta of some date in the
# past and a current date
class Transaction:
    def __init__(self, date=None, account=None, category=None, amount=None):
        self.account = account
        self.date = date
        self.amount = amount
        self.category = category

    def __repr__(self):
        return [self.date, self.account, self.category, self.amount]

    def printInfo(self):
        print(self.account + "\t" + str(self.date) + "\t" +
              str(self.amount) + "\t" + self.category)
