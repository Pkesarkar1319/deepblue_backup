import pymongo as py
import json

def get_skills():
    
    return collection.distinct('skills')

myclient = py.MongoClient("mongodb://localhost:27017/")
db = myclient["Resume"]
collection = db['data']