class Transaction:
    def __init__(self, account=None, date=None, amount=None, category=None):
        self.account = account
        self.date = date
        self.amount = amount
        self.category = category
