from pymongo import MongoClient

connection_string = "mongodb://admin:password@localhost:27017/?authSource=admin"

client = MongoClient(connection_string)

db_connection = client["meuBanco"]

print(db_connection) 