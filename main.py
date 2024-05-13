import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure, OperationFailure

def main():
    client = MongoClient("mongodb+srv://gannamalygina:ugtOWPbQtq5yzQS8@cluster0.0alrllj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    #client = MongoClient("mongodb+srv://gannamalygina:ugtOWPbQtqQS8@cluste0.0alrllj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi('1')
    )
    try:
        client.server_info()
        cats = client.test.cats
    except ConnectionFailure:
        print("Connection to the db is not established")
    except OperationFailure:
        print("Connection to the db is not established")



def find_cat_by_name(name):
    result = cats.find_one({"name": name})
    if not result:
        print (f"There is no cat {name} in the db")
    return result

def read_all_docs():
    result = cats.find({})
    for el in result:
        print(el)

def read_cat_by_name():
    input_name = input("Enter cat's name to find: ")
    print(find_cat_by_name(input_name))
        
def update_age_by_name():
    input_name = input("Enter cat's name to change its age: ")
    result = find_cat_by_name(input_name)
    input_age = input("Enter a new age: ")
    cats.update_one({"name": input_name}, {"$set": {"age": input_age}})
    print(find_cat_by_name(input_name))
    

def add_feature_by_name():
    input_name = input("Enter cat's name to add a new feature: ")
    input_feature = input("Enter a new feature: ")
    cats.update_one({"name": input_name}, {"$push": {"features": input_feature}})
    print(find_cat_by_name(input_name))

def delete_cat_by_name():
    input_name = input("Enter cat's name to delete the cat: ")
    cats.delete_one({"name": input_name})
    print(f"Cat {input_name} is deleted")

def delete_all_docs():
    cats.delete_many({})
    print("All docs are deleted")

if __name__ == "__main__":
    main()