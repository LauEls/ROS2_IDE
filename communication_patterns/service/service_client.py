from communication_patterns.service.service import Service

class ServiceClient(Service):
    def __init__(self, srv_type, raw_service_name):
        super().__init__(srv_type, raw_service_name)
        print("Service Client Name: ", self.service_name)

    