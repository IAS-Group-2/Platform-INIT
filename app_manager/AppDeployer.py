from utils.DBHelper import DBHelper
from models.Application import App
from utils import storageHelper as storage
from storage_manager import config
import os
from utils import storageHelper as storageInterface
from storage_manager import config as storage_config
from zipfile import ZipFile
import app_manager.DockerGenerator as DockerGenerator
import json
from kafka_manager.KafkaInit import Producer
import config.config as gconfig


class AppDeployer:
    def __init__(self,app_name,app_id,sensors):
        self.app_id = app_id
        self.app_name = app_name
        self.file_name = "application_"+app_id
        self.sensors = sensors
        self.local_storage_path = config.DEFAULT_DOWNLOAD_PATH
        self.dir = self.local_storage_path+"/"+self.file_name
        self.producer = Producer(gconfig.LBS_TOPIC)


    def pull_app(self):
        storage.pull_one(config.STORAGE_VM_ADDRESS+"/application_"+ self.app_id+".zip",self.local_storage_path)
        # os.remove(self.path)
    
    def generate_config(self):
        """
        Sensor_1 = "sensor_id"
        """
        with open(os.path.join(self.local_storage_path, self.file_name+"/sensor_config.py"), "w+") as f:
            for i,sensor in enumerate(self.sensors):
                f.write("Sensor_"+str(i+1)+" = \""+sensor.sensor_topic+"\"\n")
            f.write("\n")

    def extract_zip(self):
        with ZipFile(os.path.join(self.local_storage_path,  self.file_name + ".zip"), 'r') as zipObj:
            zipObj.extractall(os.path.join(self.local_storage_path, self.file_name))

    def extract_reqs(self):
        with open(self.dir+"/contract.json") as f:
            contract = json.load(f)
        #read import-files
        requirement_apt = contract["requirement-apt"]
        requirement_var = contract["requirement-var"]
        return requirement_apt, requirement_var

    def create_zip(self):
        # create a ZipFile object
        with ZipFile(self.file_name+'.zip', 'w') as zipObj:
            # Iterate over all the files in directory
            for folderName, subfolders, filenames in os.walk(self.file_name):
                for filename in filenames:
                    #create complete filepath of file in directory
                    filePath = os.path.join(folderName, filename)
                    # Add file to zip
                    zipObj.write(filePath)
    
    def ping_lbs(self,msg):
        self.producer.send_message(msg)
        print("Message sent to LBS")
        self.producer.close()

    def deploy(self):
        self.pull_app()
        self.extract_zip()
        os.remove(self.dir+'.zip')
        self.generate_config()
        requirement_apt, requirement_var = self.extract_reqs()
        DockerGenerator.create(self.dir,requirement_apt,requirement_var)
        # change directory
        cur_dir = os.getcwd()
        os.chdir(config.DEFAULT_DOWNLOAD_PATH)
        self.create_zip()
        os.chdir(cur_dir)
        os.system("rm -rf "+self.dir)
        storageInterface.push(self.dir+'.zip',storage_config.STORAGE_VM_ADDRESS_MODELS)
        msg = json.dumps({"service_name":self.dir})
        # #delete the zip file
        os.remove(self.dir+'.zip')
        self.ping_lbs(msg)



    
