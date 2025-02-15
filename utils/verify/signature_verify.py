from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os, copy
#data={
#    "adr_x": "b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0bgcafQtBBNBxqtQeXGM\nlmcbmrokj8pg9fkHXYktY7/Lf4MC3CCrJUG+obFgHYPYMh6SmTHZSBzs6zVW2HFg\n/WPdJxv0DIXlU474yTinijZgqGZEH37sxXKyjvVCWcTGF/jS0LMEo6NMIodwsTh4\nVZ5JmhpLl9bsDxeIWeF+ASxzXVEhxm7YRzk4tRhXkdy5AR2W74yjlIVpmagJ7s7O\n6AiPWqJK72cnn8z88NCiBj0HvagLMn6yEP9oZh0S/SjubVmMIM1LW2QPhusuckk1\nfh30Idv8HjE25mNj5l5dhKCXJfbLZ209g6pLYLHSCUIqajDkWUQZQgQyib5aA00K\nOQIDAQAB\n-----END PUBLIC KEY-----\n'",
#    "signature":"7c319016fdb59c780db73d15ad311e06ea326c8c549b4450e3ca59811563ea2269fbe565ebffc8e973a93eec45c33d7137b661d2bc46056fe2c0980821eb21932a48a690f7523a09286d21ba11828cf728e9858f75d1d1f38af1b12613780cdc94a496cb6778a457a061156acd3e6d634daec347b1acf7838bdeb572a4e713c90b2e493c5c88b335f7e0898558f8f80935e9b8f20981b2193db782d5a5b479cc05aab3245e86f37adb687da3664f41de5d176a7f56bb8b3c539f15b07f428a0819be956b9f358b7564d2e1caee32594443bb888033d1211044c59ec2017b788e1f0fa7765326873564c329a2fbbfb4760bf9d1bdd1b3a878237a2e967842e752",
#}
def decrypt_with_public_key(public_key_pem, signature, original_message):
    signature = bytes.fromhex(signature)
    public_key_pem=public_key_pem.encode('utf-8')
    public_key = serialization.load_pem_public_key(public_key_pem)
    try:
        public_key.verify(
            signature,
            original_message.encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True  # Verification succeeded
    except Exception as e:
        return False  # Verification failed

def is_valid(data):
    curated_data=copy.deepcopy(data)
    curated_data["signature"]=""
    curated_data=f"""{curated_data}"""
    #print(curated_data)
    if (decrypt_with_public_key(data.get("adr_x"), data.get("signature"), curated_data)):
        return True

    else:
        return False




