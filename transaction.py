class Transaction:
    def __init__(self, account=None, date=None, amount=None, category=None):
        self.account = account
        self.date = date
        self.amount = amount
        self.category = category

    def printInfo(self):
        print(self.account + "\t" + str(self.date) + "\t" +
              str(self.amount) + "\t" + self.category)
