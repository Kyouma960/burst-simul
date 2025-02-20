from utils.ledger import ledger_util
from utils.transact import validate_transaction
import time

def check():
    response=validate_transaction.is_valid_md5(method, adr_x, amount)
    return response

def send():
    validity=not(validate_transaction.expiry_check(link,method,adr_x)) 
    curated_data={
        'method': method,
        'adr_x': adr_x,
        'adr_y': adr_y,
        'amount': amount,
        'signature': signature,
        'link': link, 
        'epoch': epoch,
        'key': key
    }
    return validity, curated_data

def burn():
    timestamp_node=time.time()
    validity, response=validate_transaction.is_valid_burn(method, adr_x, amount)
    timestamp = data.get("timestamp")
    curated_data={
        'method': method,
        'adr_x': adr_x,
        'adr_y': adr_y,
        'amount': amount,
        'signature': signature,
        'timestamp': timestamp,
        'timestamp_node': timestamp_node,
        'key': key
    }
    return validity, curated_data

def transact(data):    
    response={}
    validity=False
    try:

        method= data.get("method")
        adr_x = data.get("adr_x")
        adr_y = data.get("adr_y")
        amount = data.get("amount")
        signature = data.get("signature")
        curated_data={}
        key = ledger_util.gen_md5(signature)

        if(validity):
            ledger_util.ledger_add(ledger_util.transact_path,curated_data)
        else:
            response = {"message":"Invalid Transaction.",}
    

    except:
        response = {
                "message": "Incorrect format",
                }
    return response

