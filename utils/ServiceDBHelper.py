from models.Service import Service

class ServiceDB:
    def __init__(self, dbh):
        self.db = dbh.DB
        self.col_services = self.db.services
    
    def register_service(self,service):
        """
        insert service into mongo
        service: service
        """
        self.col_services.insert_one(service.to_json())
        return "Success"

    def get_service_by_id(self,service_id):
        """
        get service from mongo
        service_id: string
        """
        service = self.col_services.find_one({"service_id":service_id})
        if service is None:
            return None
        return service(service)
    
    def get_services(self):
        """
        get all services from mongo
        """
        services = []
        for service in self.col_services.find():
            services.append(Service(service))
        return services
    
    def get_services_by_user(self,user_id):
        """
        get all services from mongo
        """
        services = []
        for service in self.col_services.find({'owner':user_id}):
            services.append(Service(service))
        return services

    def remove_service_by_id(self,service_id):
        """
        remove service from mongo
        """
        self.col_services.delete_many({'service_id':service_id})
        return "Success"