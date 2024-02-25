from communication_patterns.base import Base
    
class Service(Base):
    def __init__(self, srv_type, raw_service_name):
        self.srv_type = srv_type
        self.service_name = self.processRawName(raw_service_name)
        