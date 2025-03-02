from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

def generate_or_load_keys(private_key_file="private_key.pem", public_key_file="public_key.pem", key_size=2048,check=True):
    if check==True and os.path.exists(private_key_file) and os.path.exists(public_key_file):
        print("Keys found. Loading existing keys...")
        with open(private_key_file, "rb") as priv_file:
            private_key = priv_file.read()
        with open(public_key_file, "rb") as pub_file:
            public_key = pub_file.read()
    else:
        print("No keys found. Generating new keys...")
        private_key_obj = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )
        public_key_obj = private_key_obj.public_key()

        private_key = private_key_obj.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_key = public_key_obj.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open(private_key_file, "wb") as priv_file:
            priv_file.write(private_key)
        with open(public_key_file, "wb") as pub_file:
            pub_file.write(public_key)
        print("Keys generated and saved.")
    return private_key, public_key.decode('utf-8')

def encrypt_with_private_key(private_key_pem, message):
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    message=f"""{message}"""
    signature = private_key.sign(
        message.encode('utf-8'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature.hex()

def encrypt_message():
    private_key, public_key = generate_or_load_keys(private_key_file="private_key.pem", public_key_file="public_key.pem", key_size=2048, check=True)
    signature= encrypt_with_private_key(private_key, data)
    return public_key, signature

#data={
#    "adr_x": "b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0bgcafQtBBNBxqtQeXGM\nlmcbmrokj8pg9fkHXYktY7/Lf4MC3CCrJUG+obFgHYPYMh6SmTHZSBzs6zVW2HFg\n/WPdJxv0DIXlU474yTinijZgqGZEH37sxXKyjvVCWcTGF/jS0LMEo6NMIodwsTh4\nVZ5JmhpLl9bsDxeIWeF+ASxzXVEhxm7YRzk4tRhXkdy5AR2W74yjlIVpmagJ7s7O\n6AiPWqJK72cnn8z88NCiBj0HvagLMn6yEP9oZh0S/SjubVmMIM1LW2QPhusuckk1\nfh30Idv8HjE25mNj5l5dhKCXJfbLZ209g6pLYLHSCUIqajDkWUQZQgQyib5aA00K\nOQIDAQAB\n-----END PUBLIC KEY-----\n'",
#    "signature":"",
#}

#data=f"""{data}"""
#print(encrypt_message())
