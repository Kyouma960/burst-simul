import time
import json
from core.keys import encrypt
from template import transact, endorse, query
from core import connect
payload={}
print("What do you want to do?")
a=int(input("""
            1. Transact
            2. Endorse
            3. Consti
            4. Delegate/Revoke
            5. Query
            0. Exit
    """))

if (a==1):
    method=int(input("""
            Choose one:
            1. BRN
            2. TRST
        """))
    adr_y=input("Enter wallet address of receiver:")
    amount=int(input("How much amount would you like to send?:"))
    timestamp=time.time()
    private_key, adr_x=encrypt.generate_or_load_keys()

    if (method==1):
        payload=transact.burn(adr_x,adr_y,amount,timestamp,"")
        signature = encrypt.encrypt_with_private_key(private_key,payload)
        payload["signature"]=signature

    if (method==2):
        payload=query.check(adr_x)
        out=connect.get_req(payload)
        print(out)
        md5_choice=input("Which one?")
        payload=transact.send(adr_x,adr_y,amount,timestamp, md5_choice,"")
        signature = encrypt.encrypt_with_private_key(private_key,payload)
        payload["signature"]=signature


elif (a==2):
    adr_y=input("Enter wallet address of the one being endorsed:")
    amount=int(input("How much amount would you like to endorse:"))
    timestamp=time.time()
    private_key, adr_x=encrypt.generate_or_load_keys()
    payload=endorse.wallet(adr_x,adr_y,amount,timestamp,"")
    signature = encrypt.encrypt_with_private_key(private_key,payload)
    payload["signature"]=signature



elif (a==3):


    variant=int(input("""
    Do you want to publish or vote:
    1. Publish
    2. Vote
    """))

    private_key, adr_x=encrypt.generate_or_load_keys()

    if (method==1):
        identity=int(input("Enter the unique id of the consti submission:"))
        timestamp=time.time()
        payload=endorse.consti_vote(adr_x,identity,timestamp,"")
        signature = encrypt.encrypt_with_private_key(private_key,payload)
        payload["signature"]=signature


    if (method==2):
        data=input("""
                    Enter the consti submission that you want to make:
                   """)
        timestamp=time.time()
        payload=endorse.consti_publish(adr_x,data,timestamp,"")
        signature = encrypt.encrypt_with_private_key(private_key,payload)
        payload["signature"]=signature



elif (a==4):

    private_key, adr_x=encrypt.generate_or_load_keys()
    adr_y=input("Enter wallet address of the other wallet:")
    timestamp=time.time()
    delegate_privkey, delegate_pubkey=encrypt.generate_or_load_keys(private_key_file="./keys/delegate_private_key.pem", public_key_file="./keys/delegate_public_key.pem", key_size=2048, check=False)
    enc_privkey=encrypt.encrypt_with_private_key(adr_y,delegate_privkey)
    payload=endorse.delegate(adr_x,adr_y,delegate_pubkey,enc_privkey,timestamp,"")
    signature = encrypt.encrypt_with_private_key(private_key,payload)
    payload["signature"]=signature



elif (a==5):

    private_key, adr_x=encrypt.generate_or_load_keys()
    variant=int(input("""
            Enter what you want to know about:
            1. General info of the Wallet
            2. Wallet Points / Balance
            3. Increment value 
            4. Delegated wallet
    """))

    if (variant==1):
        payload=query.general(adr_x)
     
    if (variant==2):
        payload=query.wallet(adr_x)
     
    if (variant==3):
        payload=query.increment(adr_x)
 
    if (variant==4):
        payload=query.delegate(adr_x)
    
    out=connect.get_req(payload)
    print(out)
    sys.exit()


elif (a==0):
    sys.exit()


else:
    print("Wrong option.")

print(payload)
out=connect.post_req(payload)
print(out.json())
