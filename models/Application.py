import json

class App:
    def __init__(self,name,description,status,owner_id,app_id,storage_loc,sensor_count,is_deployed=0,is_active=0,sensor_bindings=[],is_sheduled=0):
        self.name=name
        self.description=description
        self.status=status
        self.owner_id=owner_id
        self.app_id=app_id
        #app is deployed or not
        self.zip_loc = storage_loc
        self.is_uploaded = 1
        self.is_deployed = is_deployed
        self.is_active = is_active
        self.sensor_bindings = sensor_bindings
        self.is_sheduled = is_sheduled
        self.sensor_count = sensor_count

    #update sensor bindings
    def update_sensor_bindings(self,sensor_bindings):
        self.sensor_bindings = sensor_bindings

    #update deployed status
    def update_deployed_status(self,is_deployed):
        self.is_deployed = is_deployed
    
    def update_active_status(self,is_active):
        self.is_active = is_active
    
    def update_sheduled_status(self,is_sheduled):
        self.is_sheduled = is_sheduled
    
    def get_sensor_bindings(self):
        return self.sensor_bindings
    
    
    #return a json object to insert in mongo
    def to_json(self):
        return {
            "name":self.name,
            "description":self.description,
            "status":self.status,
            "owner_id":self.owner_id,
            "app_id":self.app_id,
            "is_deployed":self.is_deployed,
            "is_active":self.is_active,
            "sensor_bindings":self.sensor_bindings,
            "is_sheduled":self.is_sheduled,
            "is_uploaded":self.is_uploaded,
            "zip_loc":self.zip_loc,
            "sensor_count":self.sensor_count
        }
    
        