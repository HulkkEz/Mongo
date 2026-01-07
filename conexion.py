from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

URI = "mongodb+srv://<USER>:<PASSWORD>@unnamed-cluster..."

client = MongoClient(URI)
db = client["Tienda"]

print("✅ Conectado al cluster MongoDB Atlas")



