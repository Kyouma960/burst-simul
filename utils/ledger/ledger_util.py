import json
import hashlib

transact_path = 'ledger/data.json'
endorse_path = 'ledger/endorse.json'
wallet_path = 'ledger/wallets.json'
consti_path = 'ledger/consti.json'
delegate_path = 'ledger/delegate.json'

def ledger_read(path):
    with open(path, "r") as file:
        ledger = json.load(file)
    return ledger 

def ledger_write(path,ledger):
    with open(path, "w") as file:
        json.dump(ledger, file, indent=4)

def gen_md5(value):
    return hashlib.md5(value.encode()).hexdigest()

def ledger_add(path, data):
    ledger=ledger_read(path)
    ledger.append(data)
    ledger_write(path,ledger) 

def ledger_scan(path, value):
    ledger_read(path)
    return [entry for entry in ledger if value in entry.values() or value in str(entry)]

#def wallets(adr_x, adr_y, amount, method, timestamp, timestamp_node):
 #   ledger=ledger_read(wallet_path)
     


#def consti(consti_path, data):


