# # coding = utf-8
# from pymongo import MongoClient
#
# client = MongoClient('mongodb://localhost:27017')
# db = client.books
# collection = db.bookdetails
# doc = {
#     'name':'King',
#     'age':'22',
#     'sex':'M',
# }
# collection.insert_one(doc)
# client.close()