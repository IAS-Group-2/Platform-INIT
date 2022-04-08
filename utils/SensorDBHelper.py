from models.Sensor import Sensor

class SensorDB:
    def __init__(self, dbh):
        self.db = dbh.DB
        self.col_sensors = self.db.sensors
    
    def register_sensor(self,sensor):
        """
        insert sensor into mongo
        sensor: Sensor
        """
        self.col_sensors.insert_one(sensor.to_json())
        return "Success"

    def get_sensor_by_id(self,sensor_id):
        """
        get sensor from mongo
        sensor_id: string
        """
        sensor = self.col_sensors.find_one({"sensor_id":sensor_id})
        if sensor is None:
            return None
        return Sensor(sensor)
    
    def get_sensors(self):
        """
        get all sensors from mongo
        """
        sensors = []
        for sensor in self.col_sensors.find():
            sensors.append(Sensor(sensor))
        return sensors
    
    def remove_sensor_by_id(self,sensor_id):
        """
        remove sensor from mongo
        """
        self.col_sensors.delete_many({'sensor_id':sensor_id})
        return "Success"