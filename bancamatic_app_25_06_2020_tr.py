import pdb 

AytacInfo = {
    "name": "Aytaç Kaşoğlu",
    "accountID": "7789523",
    "balance": 7000,
    "addiAccount": 3500,
    "accountType": "Euro"
}

RichardInfo = {
    "name": "Richard Hendriks",
    "accountID": "8456532",
    "balance": 65230,
    "addiAccount": 3000,
    "accountType": "Sterlin"
}

TimInfo = {
    "name": "Tim Cook",
    "accountID": "7576914",
    "balance": 80000,
    "addiAccount": 300500,
    "accountType": "Dollar"
}
 
BillInfo = {
    "name": "Bill Gates",
    "accountID": "8594354",
    "balance": 900000,
    "addiAccount": 80000,
    "accountType": "Dollar"
}

def giveMoney(account, amount):
    print(f"Hello {account['name']}")

    if account["balance"] >= amount:
        account["balance"] -= amount
        print("You can take money.")
    else:
        total = account["balance"] + account["addiAccount"]

        if (total >= amount):
            addiAccountUses = input("Do you wanna use your additional account? (E/H)")
            if addiAccountUses == "E":
                addiAccountAmount = amount - account["balance"]
                account["balance"] = 0
                account["addiAccount"] -= addiAccountAmount
                print("You can take your money.")

            elif addiAccountUses == "H":
                print(f"There is {account['balance']} in {account['accountID']} account.")

            else:
                print("Wrong key! Please try again.")
        else:
            print("Your balance is low for take money. Sorry!")

giveMoney(RichardInfo, 65252)

pdb.set_trace()