def storeData(username,password,role):
    import pymongo
    CONNECTION_STRING = "mongodb://20.228.199.180:3000/"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["mydatabase"]
    collection = db.registeredUsers
    required_user=collection.find_one({"user_name":username,"password":password})
    if required_user is not None:
        return "User Already Exist"    
    collection.insert_one({"user_name":username,"password":password,"roles":role})
    return "registered successfully."

def checkCredentials(username,password,role):
    import pymongo
    CONNECTION_STRING = "mongodb://20.228.199.180:3000/"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["mydatabase"]
    collection = db.registeredUsers
    required_user=collection.find_one({"user_name":username,"password":password})
    if required_user is None:
        return "Invalid Credentials"
    else:
        curr_roles=required_user["roles"]
        if role not in curr_roles:
            return "Invalid Role"
        else:
            return "Success"

def View_Users():
    import pymongo
    CONNECTION_STRING = "mongodb://20.228.199.180:3000/"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["mydatabase"]
    collection = db.registeredUsers
    allUsers=collection.find({})
    users=[]
    for user in allUsers:
        users.append(user['user_name'])
    print(users)
    return users

def deleteUser(uname):
    import pymongo
    CONNECTION_STRING = "mongodb://20.228.199.180:3000/"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["mydatabase"]
    collection = db.registeredUsers
    myquery = { "user_name": uname}
    try:
        collection.delete_one(myquery)
        return "Success"
    except:
        return "Some Error occured"

def viewRoles(uname):
    import pymongo
    CONNECTION_STRING = "mongodb://20.228.199.180:3000/"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["mydatabase"]
    collection = db.registeredUsers
    target=collection.find_one({"user_name":uname})
    return target['roles']