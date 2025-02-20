from utils.ledger import ledger_util
def is_valid(data):
    values=[]
    values.append(data.get("adr_x"))
    if(ledger_util.ledger_scan(ledger_util.transact_path,values)):
        return True
    else:
        return False
