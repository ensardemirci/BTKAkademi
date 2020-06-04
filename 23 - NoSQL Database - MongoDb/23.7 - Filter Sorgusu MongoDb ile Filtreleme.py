import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient('mongodb://localhost:27017') mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/<dbname>?retryWrites=true&w=majority
myclient = pymongo.MongoClient('mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

# result = mycollection.find_one({'_id':ObjectId('5ed87269f1db39d4f9585b99')})

# result = mycollection.find({'name':'Samsung S5'})

# result = mycollection.find({
#     'name': {
#         '$in' : ['Samsung S5','Samsung S6']
#     }
# })

# result = mycollection.find({
#     'price': {
#         '$gt': 5000
#     }
# })

# result = mycollection.find({
#     'price': {
#         '$eq': 5000
#     }
# })

# result = mycollection.find({
#     'price': {
#         '$lt': 5000
#     }
# })

result = mycollection.find({
    'name': {'$regex':'^S'}
})


for i in result:
    print(i)

# print(result)
