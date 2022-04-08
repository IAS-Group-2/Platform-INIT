import json
class Sensor:
    def __init__(self,sensor_data):
        """
        Initialise sensor object
        data: {
            "sensor_name":"demo",
            "sensor_id":"s23",
            "sensor_topic":"s23",
            "sensor_loc":"Front Camera"
            "sensor_type":"Camera",
            "sensor_description":"Laptop's front camera"
        }
        """
        self.sensor_name = sensor_data["sensor_name"]
        self.sensor_id = sensor_data["sensor_id"]
        self.sensor_topic = sensor_data["sensor_topic"]
        self.sensor_loc = sensor_data["sensor_loc"]
        self.sensor_type = sensor_data["sensor_type"]
        self.sensor_description = sensor_data["sensor_description"]
    
    def to_json(self):
        return {
            "sensor_name":self.sensor_name,
            "sensor_id":self.sensor_id,
            "sensor_topic":self.sensor_topic,
            "sensor_loc":self.sensor_loc,
            "sensor_type":self.sensor_type,
            "sensor_description":self.sensor_description
        }