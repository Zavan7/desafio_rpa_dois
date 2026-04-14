from pymongo import MongoClient

connection_str = 'mongodb://localhost:27017/'
client = MongoClient(connection_str)
db_collection = client['automation_db']

collection = db_collection.get_collection('automation_two')

print(db_collection)
print(collection)

search_filter = {
    '345': '123'
}

collection.update_one(
    search_filter,
    {'$set': search_filter}
    )

response = collection.find(search_filter)

for r in response:
    print(r)