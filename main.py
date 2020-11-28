import account
import transaction
import json
import csv

# load contents of json file
imported = {}
with open("data1.json", "r") as f:
    accounts = json.load(f)
# instantiate contents as account objects
for key, value in accounts.items():
    imported[key] = account.Account(
        accounts[key]['name'], accounts[key]['accountType'], account.date(accounts[key]['date'][0], accounts[key]['date'][1], accounts[key]['date'][2]), accounts[key]['balance'])

# importing CSV data
filename = "transactions.csv"

# rows and columns
fields = []
rows = []
transactions = []

# reading csv file
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        # rows.append(transaction.Transaction(
        #     row['Card'], row['Date'], row['Amount'], row['Category']))
print(fields)
for x in rows:
    trans = transaction.Transaction(x[2], x[0], x[4], x[3])
    transactions.append(trans)

print(transactions)
# Save contents of account objects to json file
with open("data1.json", "w") as f:
    json.dump(accounts, f, default=account.transform)
