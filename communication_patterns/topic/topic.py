from communication_patterns.base import Base

class Topic(Base):
    def __init__(self, msg_type, raw_topic_name, qos_profile):
        self.msg_type = msg_type
        self.qos_profile = qos_profile

        self.topic_name = self.processRawName(raw_topic_name)
