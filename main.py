import account
import json

# load contents of json file
imported = {}
with open("data1.json", "r") as f:
    accounts = json.load(f)
# instantiate contents as account objects
for key, value in accounts.items():
    imported[key] = account.Account(
        accounts[key]['name'], accounts[key]['accountType'], account.date(accounts[key]['date'][0], accounts[key]['date'][1], accounts[key]['date'][2]), accounts[key]['balance'])
# Save contents of account objects to json file
with open("data1.json", "w") as f:
    json.dump(accounts, f, default=account.transform)
