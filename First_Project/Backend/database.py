from pymongo import MongoClient

connection_string = "mongodb://admin:password@localhost:27017/?authSource=admin"

client = MongoClient(connection_string)

db_connection = client["meuBanco"]

collection = db_connection.get_collection("Mingacollection")

print(collection) 
