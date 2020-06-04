import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient('mongodb://localhost:27017') mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/<dbname>?retryWrites=true&w=majority
myclient = pymongo.MongoClient('mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

# update_one
# update_many

# mycollection.update_one(
#     {'name':'Samsung S6'},
#     {'$set':{
#         'name':'Iphone 7'
#     }}
# )

mycollection.update_many(
    {'name':'Samsung S7'},
    {'$set':{
        'name':'Iphone 8',
        'price': 5000
    }}
)



for i in mycollection.find():
    print(i)