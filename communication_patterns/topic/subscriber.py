from communication_patterns.topic.topic import Topic

class Subscriber(Topic):
    def __init__(self, msg_type, topic_name, qos_profile):
        super().__init__(msg_type, topic_name, qos_profile)
        print("Subscriber Name: ", self.topic_name)

    