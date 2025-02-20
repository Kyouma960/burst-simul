from utils.ledger import ledger_util
from utils.transact import validate_transaction
import time

def check(method, adr_x):
    response=validate_transaction.is_valid_md5(method, adr_x, amount)
    return response

def send(link, method, adr_x):
    epoch, validity=not(validate_transaction.expiry_check(link,method,adr_x)) 
    return validity, epoch

def burn(method, adr_x ,amount):
    validity=validate_transaction.is_valid_burn(method, adr_x, amount)
    return validity

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
        
        if(method=='burn'):
            validity=burn(method,adr_x,amount)
            curated_data={
                'method': method,
                'adr_x': adr_x,
                'adr_y': adr_y,
                'amount': amount,
                'signature': signature,
                'timestamp': timestamp,
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
                'amount': amount,
                'signature': signature,
                'link': link, 
                'epoch': epoch,
                'key': key
            }

     
        if(validity):
            ledger_util.ledger_add(ledger_util.transact_path,curated_data)
        else:
            response = {"message":"Invalid Transaction.",}
    

    except:
        response = {
                "message": "Incorrect format",
                }
    return response

