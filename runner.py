# IMPORTS
import json
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
a = input("--[statistics] (1) or [probability] (2)?:  ")
if a=="statistics" or a=="1":
    from statistics_lib.operations import observType
    x = input(f"--Select observation type - {list(observType.keys())}:  ")
    className = observType[x]
    runnerObj = className()
    runnerObj.get_output()
elif a=="probability" or a=="2":
    from probability_lib.operations import distType
    x = input(f"--Select distribution type - {list(distType.keys())}:  ")
    className = distType[x]
    runnerObj = className()
    runnerObj.get_output()
else:
    raise ImportError("You should import correct library!")