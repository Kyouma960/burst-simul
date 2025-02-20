def send(adr_x, adr_y, amount, timestamp, link, signature):
    return {
        'type':'transaction',
        'method':'send',
        'adr_x': adr_x,
        'adr_y': adr_y,
        'amount': amount,
        'timestamp': timestamp,
        'signature': signature,
        'link': link
    }
    

def burn(adr_x,adr_y, amount, timestamp, signature):
     return {
        'type':'transaction',
        'method':'burn',
        'adr_x': adr_x,
        'adr_y': adr_y,
        'amount': amount,
        'timestamp': timestamp,
        'signature': signature,
    }
