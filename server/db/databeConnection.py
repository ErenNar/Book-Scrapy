from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv
import os
load_dotenv()

connect = MongoClient("mongodb://localhost:27017")
db = connect["productFollowDb"]
collection = db["productTbl"]

try:
    info = connect.server_info() 
    print("server connect successful")
except ServerSelectionTimeoutError:
    print("server is down.")


connect.close()
