from utils.ledger import ledger_util
import time
rate_increment=10 #minutely rate

def is_valid(method, adr_x, amount, key ):
    if (method=='burn'):
        total=0
        timestamps=[]
        ledger_list=ledger_util.ledger_scan(adr_x,method)
        for item in ledger_list:
            if (item.get("adr_x") == adr_x):
                total=total+int(item.get("amount"))
                timestamps.append(item.get("timestamp_node"))
        epoch=min(timestamps)
        total=total+amount
        wallet_increment=(time.time()-epoch)*(rate_increment/60))
        if (total<wallet_increment):
            response={
                'message':'Fund transferred!'
            }
            return True
        else:
            response={
                'message':'No balance, you need more funds.'
            }
            return False

    if (method=='send'):
        total_send=0
        total_receive=0
        ledger_list=ledger_util.ledger_scan(adr_x)
        for item in ledger_list:
            if (item.get("adr_y") == adr_x):
                total_receive=total_receive+int(item.get("amount"))
            if (item.get("adr_x") == adr_x):
                total_send=total_send+int(item.get("amount"))
        total_send=total_send+amount
        if (total_receive<total_send):



