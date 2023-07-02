#Taylor Jacobs
#CYBR410 - Database Security
#Prof. Peter Haas
#7/2/2023

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.utbzgbt.mongodb.net/pytech"

client = MongoClient(url)

print("\n **DB Collection List**")
db = client.pytech

print(db.list_collection_names())

input("\nPress any key to quit ")