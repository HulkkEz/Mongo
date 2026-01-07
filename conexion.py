from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

URI = "mongodb+srv://unnamed-user:IxOJzt2XYMgjY4ET@unnamed-cluster.kkvxrtg.mongodb.net/?appName=unnamed-cluster"

client = MongoClient(URI)
db = client["Tienda"]

print("✅ Conectado al cluster MongoDB Atlas")


