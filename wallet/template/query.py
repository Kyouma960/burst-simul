def general(adr_x):
    payload={
        'type':'get',
        'method':'general',
        'adr_x':adr_x,

    }
    return payload 

def wallet(adr_x):
    payload={
        'type':'get',
        'method':'wallet',
        'adr_x':adr_x,

    }
    return payload 


def increment(adr_x):
    payload={
        'type':'get',
        'method':'increment',
        'adr_x':adr_x,
    }
    return payload

def delegate(adr_x):
    payload={
        'type':'get',
        'method':'delegate',
        'adr_x':adr_x,

    }
    return payload 
   
