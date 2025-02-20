from utils.ledger import ledger_util
from utils.transact import validate_transaction
import time
timestamp_node=time.time()

def transact(data):    
    response={}
    validity=False
    try:

        if(data.get("method")=="send" or data.get("method")=="burn"):
            method= data.get("method")
            adr_x = data.get("adr_x")
            adr_y = data.get("adr_y")
            amount = data.get("amount")
            signature = data.get("signature")
            curated_data={}
            key = ledger_util.gen_md5(signature)


            if (method=='burn'):

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

            if (method=='send'):

                response=validate_transaction.is_valid_md5(method, adr_x, amount)
                #user_md5=input("Enter which one do you want to send:\n")
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


            if(validity):
                ledger_util.ledger_add(ledger_util.transact_path,curated_data)
            else:
                response = {"message":"Invalid Transaction.",}
        

    except:
        response = {
                "message": "Incorrect format",
                }
    return response

