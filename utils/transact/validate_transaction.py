from utils.ledger import ledger_util
import time

rate_increment=10 #minutely rate
expiry_time=8 #hours

def expiry_check(link, adr_x):
    values=[adr_x]
    ledger_list=ledger_util.ledger_scan(ledger_util.transact_path, values)
    for item in ledger_list:
        if (item.get("key")==link):
            epoch=item.get("epoch", link)

    for item in ledger_list:
        if(item.get("key")==epoch):
            epoch_time=item.get("timestamp_node")
            if((time.time()-epoch_time)<(expiry_time*60*60)):
                return epoch, True
            else:
                return epoch, False

def is_valid_burn(method, adr_x, amount):
    if (method=='burn'):
        total=0
        timestamps=[]
        values=[adr_x, method]
        ledger_list=ledger_util.ledger_scan(ledger_util.transact_path, values)
        print(ledger_list)
        for item in ledger_list:
            if (item.get("adr_x") == adr_x):
                try:
                    total=total+int(item.get("amount"))
                except:
                    print("Something wrong with amount")
                timestamps.append(item.get("timestamp_node"))
        wallet_epoch=min(timestamps)
        wallet_increment=(time.time()-wallet_epoch)*(rate_increment/60)
        if ((total+amount)<wallet_increment):
            response={
                'message':'Fund transferred!'
            }
            return True, (wallet_increment-total)
        else:
            response={
                'message':'No balance, you need more funds.'
            }
            return False, (wallet_increment-total)

def is_valid_md5(adr_x):
    md5_receive_list=[]
    md5_send_list=[]
    amount_list={}
    values=[adr_x]
    ledger_list=ledger_util.ledger_scan(ledger_util.transact_path, values)
    print(ledger_list)
    for item in ledger_list:
        if (item.get("adr_y") == adr_x):
            key_temp=item.get("key")
            md5_receive_list.append(item.get("key"))
            amount_list[key_temp] = item.get("amount")

        if (item.get("adr_x") == adr_x and item.get("method")=="send"):
            md5_send_list.append(item.get("link"))
    print(md5_receive_list)
    md5_list=list(set(md5_receive_list) - set(md5_send_list))
    valid_amounts = {md5: amount_list.get(md5, 0) for md5 in md5_list}

    if (md5_list):
        response={
                'message' : 'These are the ones that can be transferred',
                'md5_list' : md5_list,
                'amount_list': valid_amounts
        }
        return response
    else:
        response={
            'message':'Not possible'
        }
        return response 


