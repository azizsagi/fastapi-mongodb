from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:dasdasdsd@cluster0.2lzgtyq.mongodb.net/?retryWrites=true&w=majority",tls=True, tlsAllowInvalidCertificates=True)

database = client.users_db

collection_name = database["user_collection"]