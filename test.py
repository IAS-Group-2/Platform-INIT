from utils.DBHelper import DBHelper
from models.Application import App

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

print(mongo.getApplications())
# print(mongo.removeApplications())
