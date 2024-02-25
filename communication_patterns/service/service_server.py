from communication_patterns.service.service import Service

class ServiceServer(Service):
    def __init__(self, srv_type, raw_service_name):
        super().__init__(srv_type, raw_service_name)
        print("Service Server Name: ", self.service_name)

    