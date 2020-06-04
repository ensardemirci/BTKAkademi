import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient('mongodb://localhost:27017') mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/<dbname>?retryWrites=true&w=majority
myclient = pymongo.MongoClient('mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

# result = mycollection.find().sort('name', -1)
# result = mycollection.find().sort('price', -1)
result = mycollection.find().sort([('name',1),('price',-1)])

for i in result:
    print(i)