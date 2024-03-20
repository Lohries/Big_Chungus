from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"

client = MongoClient(connection_string)

db_connection = client["meuBanco"]

collection = db_connection.get_collection("minhaCollection")

print(collection) 

search_filter = { "hello" : "world"}
search_filter2 = { "world" : "hello"}

response1 = collection.find(search_filter)
response2 = collection.find(search_filter2)






collection.insert_one({ 
    "Let's" : "fucking go",
    "Numbers" : [144, 122, 99]
})