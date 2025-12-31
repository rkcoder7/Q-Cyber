from pymongo import MongoClient
c=MongoClient("mongodb://localhost:27017/")
db=c["Q-Defender"]
print("AES records:", db["AES encryption"].count_documents({}))
print("Key Vault:", db["Key Vault"].count_documents({}))
print("Key Cipher:", db["Key Cipher"].count_documents({}))