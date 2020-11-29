import account
import transaction
import json
import csv

# load contents of json file
imported = {}
with open("account-data.json", "r") as f:
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
        rows.append([float(row[0]), row[2], row[3], float(row[4])])

# move transactions into local list
print(fields)
for x in rows:
    # kinda dont like the way the numbers on this one work, I'm probably going to come back and change it
    trans = transaction.Transaction(x[0], x[1], x[2], x[3])
    transactions.append(trans)

# this is to test that the transactions are in the list properly
for x in transactions:
    x.printInfo()

with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in transactions:
        csvwriter.append()
# Save contents of account objects to json file
# with open("account-data.json", "w") as f:
#     json.dump(accounts, f, default=account.transform)
