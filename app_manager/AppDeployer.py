from utils.DBHelper import DBHelper
from models.Application import App
from utils import storageHelper as storage
from storage_manager import config
import os
from zipfile import ZipFile

class AppDeployer:
    def __init__(self,app_name,app_id,sensors):
        self.app_id = app_id
        self.app_name = app_name
        self.file_name = "application_"+app_id
        self.sensors = sensors
        self.local_storage_path = config.DEFAULT_DOWNLOAD_PATH

    def pull_app(self):
        storage.pull_one(config.STORAGE_VM_ADDRESS+"/application_"+ self.app_id+".zip",self.local_storage_path)
        # os.remove(self.path)
    
    def generate_config(self):
        """
        Sensor_1 = "sensor_id"
        """
        with open(os.path.join(self.local_storage_path, self.file_name+"/"+self.app_name+"/sensor_config.py"), "w+") as f:
            for i,sensor in enumerate(self.sensors):
                f.write("Sensor_"+str(i+1)+" = \""+sensor.sensor_topic+"\"\n")
            f.write("\n")

    def extract_zip(self):
        with ZipFile(os.path.join(self.local_storage_path,  self.file_name + ".zip"), 'r') as zipObj:
            zipObj.extractall(os.path.join(self.local_storage_path, self.file_name))

    def deploy(self):
        self.pull_app()
        self.extract_zip()
        self.generate_config()

    
