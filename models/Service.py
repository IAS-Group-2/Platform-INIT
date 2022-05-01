import json

class Service:
    """
    Service:

    Name: String
    Id: String
    Location: String
    Topic: String
    Discription: String
    Owner: String
    IsDeployed: string
    """ 
    def __init__(self,service_data):
        # self.name=name
        # self.id=id
        # self.location=location
        # self.topic=topic
        # self.description=description
        # self.owner=owner
        # self.is_deployed=is_deployed
        self.name = service_data["name"]
        self.id = service_data["id"]
        self.location = service_data["location"]
        self.topic = service_data["topic"]
        self.description = service_data["description"]
        self.owner = service_data["owner"]
        self.is_deployed = service_data["is_deployed"]

    
    def to_json(self):
        return {
            "name":self.name,
            "id":self.id,
            "location":self.location,
            "topic":self.topic,
            "description":self.description,
            "owner":self.owner,
            "is_deployed":self.is_deployed
        }