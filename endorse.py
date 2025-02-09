from utils.wallet import wallet_endorse_check
from utils.consti import consti_vote, consti_publish
from utils.wallet import delegate
from utils.wallet import revoke
def endorse(data):    
    try:
        if(data.get("method")=="wallet"):
            wallet_endorse_check(data.get("adr_x"),data.get("adr_y"),data.get("amount"))

        elif(data.get("method")=="consti"):
            
            if(data.get("variant")=="vote"):
                consti_vote(data.get("adr_x"),data.get("identity"))

            elif(data.get("variant")=="publish"):
                consti_publish(data.get("adr_x"),data.get("adr_y"),data.get("data"))

        elif(data.get("method")=="delegate"):
            delegate(data.get("adr_x"),data.get("adr_y"),data.get("pubkey"),data.get("enc_privkey"))

        elif(data.get("method")=="revoke"):
            revoke(data.get("adr_x"),data.get("pubkey"))

    except:
        response = {
                "message": "Incorrect format",
                }
    return response
