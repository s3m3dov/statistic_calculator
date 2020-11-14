# IMPORTS
import json
from statistic_lib.operations import dataTypes, observType, Ungrouped
#Read Json
with open('account.json', 'r') as acc1:
    acc = json.load(acc1)
# Input Part and Reading commands
#Get Name
if acc["name"] == "":
    acc["name"] = input("--Please, enter your name:  ")
    with open('account.json', 'w') as acc2:
        json.dump(acc, acc2)
else:
    pass
print(f"--Welcome, {acc['name']}.")
#Get Observation Type
x = input(f"--Select observation type from {list(observType.keys())}:  ")
className = observType[x]

runnerObj = className()
runnerObj.get_output()