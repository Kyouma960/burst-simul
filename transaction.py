from utils.ledger import ledger_util
from utils.transact import validate_transaction
import time

def check(method, adr_x):
    response=validate_transaction.is_valid_md5(method, adr_x)
    return response

def send(link, method, adr_x):
    epoch, validity=not(validate_transaction.expiry_check(link,method,adr_x)) 
    return validity, epoch

def burn(method, adr_x ,amount):
    validity, balance=validate_transaction.is_valid_burn(method, adr_x, amount)
    return validity, balance

def transact(data):    
    try:
        
        response={}
        validity=False
        method= data.get("method")
        adr_x = data.get("adr_x")
        adr_y = data.get("adr_y")
        signature = data.get("signature")
        curated_data={}
        key = ledger_util.gen_md5(signature)
        
        if(method=='burn'):

            amount = data.get("amount")
            validity, balance =burn(method,adr_x,amount)
            curated_data={
                'method': method,
                'adr_x': adr_x,
                'adr_y': adr_y,
                'amount': amount,
                'signature': signature,
                'timestamp_node': time.time(),
                'key': key
            }
        

        if(method=='check'):

            response=check(method,adr_x)
            return response

        if(method=='send'):
            link=data.get("link")
            validity,epoch=send(link,method,adr_x)
            curated_data={
                'method': method,
                'adr_x': adr_x,
                'adr_y': adr_y,
                'signature': signature,
                'link': link, 
                'epoch': epoch,
                'key': key
            }

        if(validity):
            ledger_util.ledger_add(ledger_util.transact_path,curated_data)
            response = {"message":"Valid", "balance":balance-amount}
        else:
            response = {"message":"Invalid Transaction.", "balance": balance}
    

    except Exception as e:
        print(e)
        response = {
                "message": "Incorrect format"
                }
    return response

