import pymongo
#import app model
from models.Application import App

class DBHelper:
    def __init__(self):
        self.CONN = "mongodb://20.228.199.180:3000/"
        self.CLIENT = pymongo.MongoClient(self.CONN)
        self.DB = self.CLIENT["mydatabase"]
        self.REGT_USER = self.DB["registeredUsers"]
        self.applications = self.DB["applications"]
    
    def storeData(self,username,password,role):       
        required_user=self.REGT_USER.find_one({"user_name":username,"password":password})
        if required_user is not None:
            return "User Already Exist"    
        self.REGT_USER.insert_one({"user_name":username,"password":password,"roles":role})
        return "registered successfully."

    def checkCredentials(self,username,password,role):
        required_user=self.REGT_USER.find_one({"user_name":username,"password":password})
        if required_user is None:
            return "Invalid Credentials"
        else:
            curr_roles=required_user["roles"]
            if role not in curr_roles:
                return "Invalid Role"
            else:
                return "Success"

    def View_Users(self):
        allUsers=self.REGT_USER.find({})
        users=[]
        for user in allUsers:
            users.append(user['user_name'])
        print(users)
        return users

    def deleteUser(self,uname):
        myquery = { "user_name": uname}
        try:
            self.REGT_USER.delete_one(myquery)
            return "Success"
        except:
            return "Some Error occured"

    def viewRoles(self,uname):
        target=self.REGT_USER.find_one({"user_name":uname})
        return target['roles']

    #get all users data
    def getAllUsers(self):
        allUsers=self.REGT_USER.find({})
        users=[]
        for user in allUsers:
            users.append(user)
        return users
    
    def registerApp(self,App):
        self.applications.insert_one(App.to_json())
        return "Success"
    
    def getApplications(self):
        allApps=self.applications.find({})
        apps=[]
        for app in allApps:
            tempApp = App(app['name'],app['description'],app['status'],app['owner_id'],app['app_id'],app['zip_loc'],app['sensor_count'],app['is_deployed'],app['is_active'],app['sensor_bindings'],app['is_sheduled'])
            apps.append(tempApp)
        return apps
    
    def removeApplications(self):
        self.applications.delete_many({})
        return "Success"
    
    def getAppByOwner(self,owner_id):
        allApps=self.applications.find({"owner_id":owner_id})
        apps=[]
        #convert the json to Applications
        for app in allApps:
            tempApp = App(app['name'],app['description'],app['status'],app['owner_id'],app['app_id'],app['zip_loc'],app['sensor_count'],app['is_deployed'],app['is_active'],app['sensor_bindings'],app['is_sheduled'])
            apps.append(tempApp)
        return apps
    
    def getAppById(self,app_id):
        app=self.applications.find_one({"app_id":app_id})
        tempApp = App(app['name'],app['description'],app['status'],app['owner_id'],app['app_id'],app['zip_loc'],app['sensor_count'],app['is_deployed'],app['is_active'],app['sensor_bindings'],app['is_sheduled'])
        return tempApp

