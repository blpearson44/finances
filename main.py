import account
import json

wf = account.Account("Wells Fargo", "Checking",
                     account.date(2012, 8, 20), 1000)
with open("data1.json", "w") as f:
    json.dump(wf, f, default=account.transform)

with open("data1.json", "r") as f:
    data = json.load(f)

a1 = account.Account()
a1.loadInfo(data)
a1.printInfo()
