from utils.ledger import ledger_util
import time
rate_increment=10 #minutely rate
expiry_time=2 #hours
def is_expired(epoch,ledger_list):
    for item in ledger_list:
        if(item.get("key")==epoch):
            epoch_time=item.get("timestamp_node")
        if((time.time()-epoch_time)<(expiry_time*60*60)):
                False
        else:
                True

def is_valid_burn(method, adr_x, amount):
    if (method=='burn'):
        total=0
        timestamps=[]
        values=[method, adr_x]
        ledger_list=ledger_util.ledger_scan(ledger_util.transact_path, values)
        for item in ledger_list:
            if (item.get("adr_x") == adr_x):
                total=total+int(item.get("amount"))
                timestamps.append(item.get("timestamp_node"))
        wallet_epoch=min(timestamps)
        wallet_increment=(time.time()-wallet_epoch)*(rate_increment/60))
        if ((total+amount)<wallet_increment):
            response={
                'message':'Fund transferred!'
            }
            return True, response
        else:
            response={
                'message':'No balance, you need more funds.'
            }
            return False, response

def is_valid_send(method,adr_x,amount):
    if (method=='send'):
        md5_receive_list=[]
        md5_send_list=[]
        amount_list={}
        values=[adr_x]
        ledger_list=ledger_util.ledger_scan(ledger_util.transact_path, values)

        for item in ledger_list:
            if (item.get("key")==link):
                epoch=item.get("epoch", link)

            if (item.get("adr_y") == adr_x):
                key_temp=item.get("key")
                md5_receive_list.append(item.get("key"))
                amount_list[key_temp] = item.get("amount")
 
            if (item.get("adr_x") == adr_x):
                md5_send_list.append(item.get("link"))
        md5_list=list(set(md5_receive_list) - set(md5_send_list))
        valid_amounts = {md5: amount_list.get(md5, 0) for md5 in md5_list}

        if (md5_list and not is_expired(epoch)):
            response={
                    'message' : 'These are the ones that can be transferred'
                    'md5_list' : md5_list
                    'amount_list': valid_amounts
            }
            return True, response
        else:
            response={
                'message':'Not possible'
            }
            return False, response 

