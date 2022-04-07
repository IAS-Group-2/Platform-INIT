import utils.extract_validate as extract_validate
import service_manager.DockerGenerator as DockerGenerator
from utils import storageHelper as storageInterface
from storage_manager import config as storage_config
from zipfile import ZipFile
from kafka_manager.KafkaInit import Producer, Consumer
import os
import config.config as config
import json

class Director:
    def __init__(self,lastindex):
        #create data.json file
        self.last_index = lastindex
        self.dir = "service_"+str(self.last_index)
        self.producer = Producer(config.LBS_TOPIC)
        self.setup_Dir()
    
    def create_zip(self):
        # create a ZipFile object
        with ZipFile(self.dir+'.zip', 'w') as zipObj:
            # Iterate over all the files in directory
            for folderName, subfolders, filenames in os.walk(self.dir):
                for filename in filenames:
                    #create complete filepath of file in directory
                    filePath = os.path.join(folderName, filename)
                    # Add file to zip
                    zipObj.write(filePath)
        

    def setup_Dir(self):
        #create a directory model#lastindex
        os.mkdir(self.dir)

    def is_valid(self):
        validation_val=extract_validate.validation(self.last_index,self.dir)
        return validation_val


    def ping_lbs(self,msg):
        self.producer.send_message(msg)
        print("Message sent to LBS")
        self.producer.close()

    def upload(self):
        print("Start of upload...")
        DockerGenerator.create(self.dir,[])
        self.create_zip()
        os.system("rm -rf "+self.dir)
        storageInterface.push(self.dir+'.zip',storage_config.STORAGE_VM_ADDRESS_MODELS)
        msg = json.dumps({"service_name":self.dir})
        #delete the zip file
        os.remove(self.dir+'.zip')
        self.ping_lbs(msg)
        

