from utils.DBHelper import DBHelper
from models.Sensor import Sensor
from utils.SensorDBHelper import SensorDB
from utils import storageHelper as storage
from storage_manager import config
# import config.config as config
# from kafka_manager.KafkaInit import Producer,Consumer


# producer = Producer("test_consumer")
# msg = "test message"
# producer.send_message(msg)

# print(config.UPLOAD_FOLDER)

mongo = DBHelper()
# # #print all users
# # print(mongo.getAllUsers())

# # #model app object
# # app = App("Demo App", "This is a demo app", "active", "user1", "app1")

# # #register an application
# # mongo.registerApp(app)

sensordb = SensorDB(mongo)

sensor = {
    "sensor_name":"Camera_02",
    "sensor_id":"c02",
    "sensor_topic":"camera_02",
    "sensor_loc":"pc_sahu",
    "sensor_type":"Camera",
    "sensor_description":"Laptop's front camera"
}

# sensor = Sensor(sensor)
# sensordb.remove_sensor_by_id('s23')
# sensordb.register_sensor(sensor)
# print(sensordb.get_sensors())

sensors = sensordb.get_sensors()
for sensor in sensors:
    print(sensor.to_json())

#print application jsons
# apps = mongo.getApplications()
# for app in apps:
#     print(app.to_json())

# storage.pull_one(config.STORAGE_VM_ADDRESS+"/application_"+"030"+".zip",config.DEFAULT_DOWNLOAD_PATH)

# print(mongo.removeApplications())
