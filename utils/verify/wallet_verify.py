from utils/ledger import ledger_util
def is_valid(data):
    if(ledger_util.ledger_scan(ledger_util.wallet_path,adr_x)):
        return True
    else:
        return False
