import pymongo

# myclient = pymongo.MongoClient('mongodb://localhost:27017') mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/<dbname>?retryWrites=true&w=majority
myclient = pymongo.MongoClient('mongodb+srv://ensardemirci:gvqQjRi0rXa0yIvq@cluster0-ib6ob.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

# product = {'name':'Samsung S5','price':2000}

# result = mycollection.insert_one(product)
#
# print(result)
# print(type(result))
# print(result.inserted_id)

productList = [
    {'name': 'Samsung S6', 'price': 3000, 'description': 'İyi telefon'},
    {'name': 'Samsung S7', 'price': 4000, 'categories': ['telefon','elektronik']},
    
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)