import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient('mongodb://localhost:27017') mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/<dbname>?retryWrites=true&w=majority
myclient = pymongo.MongoClient('mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

# delete_one
# delete_many

for i in mycollection.find():
    print(i)

print('*'*50)

# mycollection.delete_one({'name':'Samsung S5'})
# mycollection.delete_many({'name':{'$regex':'^S'}})

result = mycollection.delete_many({})
print(f'{result.deleted_count} adet kayıt silindi')

for i in mycollection.find():
    print(i)
