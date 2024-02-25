from communication_patterns.base import Base
    
class Action(Base):
    def __init__(self, action_type, raw_action_name):
        self.action_type = action_type
        self.action_name = self.processRawName(raw_action_name)