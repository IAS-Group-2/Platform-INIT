#import mongodb
from utils.DBHelper import DBHelper
from models.Application import App
from utils import storageHelper as storage
from storage_manager import config
import os

class AppDirector:

    def __init__(self,app,path):
        self.app = app
        self.path = path
    
    def sync_db(self):
        db = DBHelper()
        db.registerApp(self.app)
    
    def push_app(self):
        storage.push(self.path,config.STORAGE_VM_ADDRESS)
        os.remove(self.path)
        
    
