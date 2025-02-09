def wallet(adr_x, adr_y, amount,timestamp,signature):
    payload={
        'type':'endorse',
        'method':'wallet',
        'adr_x': adr_x,
        'adr_y': adr_y,
        'amount': amount,
        'timestamp': timestamp,
        'signature': signature,
    }
    return payload

def consti_vote(adr_x,id,timestamp,signature):
    payload={
        'type':'endorse',
        'method':'consti',
        'variant':'vote',
        'adr_x':adr_x,
        'identity': id,
        'timestamp': timestamp,
        'signature': signature,
    }
    return payload

def consti_publish(adr_x,data,timestamp,signature):
    payload={
        'type':'endorse',
        'method':'consti',
        'variant':'publish',
        'adr_x':adr_x,
        'data' : data,
        'timestamp': timestamp,
        'signature': signature,
    }
    return payload

def delegate(adr_x,adr_y,pubkey,enc_privkey,timestamp,signature):
    payload={
        'type':'endorse',
        'method':'delegate',
        'adr_x':adr_x,
        'adr_y':adr_y,
        'pubkey':pubkey,
        'enc_privkey':enc_privkey,
        'timestamp': timestamp,
        'signature': signature,
    }
    return payload

def revoke(adr_x,pubkey,timestamp,signature):
    payload={
        'type':'endorse',
        'method':'revoke',
        'adr_x': adr_x,
        'pubkey': pubkey,
        'timestamp': timestamp,
        'signature': signature,
    }
    return payload
