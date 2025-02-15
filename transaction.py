from utils.ledger import ledger_util
from utils.transact import validate_transaction
import time
timestamp_node=time.time()
def transact(data):    
    response={}
    try:

        if(data.get("method")=="send" or data.get("method")=="burn"):
            method= data.get("method")
            adr_x = data.get("adr_x")
            adr_y = data.get("adr_y")
            amount = data.get("amount")
            signature = data.get("signature")
            timestamp = data.get("timestamp")
            key=None
            if (method=='burn'):
                key = ledger_util.gen_md5(signature)
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

            if(validate_transaction.is_valid(method, adr_x, amount,key)):
                ledger_util.ledger_add(ledger_util.transact_path,curated_data)
            else:
                response = {"message":"Invalid Transaction.",}
        

    except:
        response = {
                "message": "Incorrect format",
                }
    return response

