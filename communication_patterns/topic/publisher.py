from communication_patterns.topic.topic import Topic

class Publisher(Topic):
    def __init__(self, msg_type, topic_name, qos_profile):
        super().__init__(msg_type, topic_name, qos_profile)
        print("Publisher Name: ", self.topic_name)

    