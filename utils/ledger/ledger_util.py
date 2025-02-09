import json

transact_path = 'ledger/data.json'
endorse_path = 'ledger/endorse.json'
wallet_path = 'ledger/wallets.json'
consti_path = 'ledger/consti.json'

def ledger_add(path, data):
    with open(path, "r") as file:
        ledger = json.load(file)
    ledger.append(data)
    with open(path, "w") as file:
        json.dump(ledger, file, indent=4)

def ledger_scan(path, **kwargs):
    with open(path, "r") as file:
        ledger = json.load(file)
     


#def prune(path, data):

#def send(path, data):

#def endorse(path, data):

#def consti(path, data):

#def delegate(path, data):

#def revoke(path, data):

    
