from cryptography.fernet import  Fernet
def encrypt_message(message, key = None):

    if key is None:
        key = Fernet.generate_key()
        f = Fernet(key)
        return f.encrypt(message), key
    else:
        f = Fernet(key)
        return f.decrypt(message)

message = "Jonn Wick is Best"
print("Original Text: " + message)
# Getting Encrypted Message and the encryption key
encMsg, key = encrypt_message(message.encode("utf-8")) # Casting strings to bytes
print(f"Encrypted Message: {encMsg.decode()}\nEncryption Key: {key.decode()}")
# Decrypting the message using the key
msg = encrypt_message(encMsg, key).decode()
print("Decrypted Message: ", msg)
