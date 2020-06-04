import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient('mongodb://localhost:27017') mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/<dbname>?retryWrites=true&w=majority
myclient = pymongo.MongoClient('mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

# result = mycollection.find_one()
for i in mycollection.find({},{'_id':0,'name':1}):
    print(i)
# print(result)
