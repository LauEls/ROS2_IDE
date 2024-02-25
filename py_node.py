import os
import re
from node import Node
from parse_util import findChar, preProcess
from communication_patterns.topic.publisher import Publisher
from communication_patterns.topic.subscriber import Subscriber
from communication_patterns.service.service_server import ServiceServer
from communication_patterns.service.service_client import ServiceClient
from communication_patterns.action.action_server import ActionServer    
from communication_patterns.action.action_client import ActionClient

class PythonNode(Node):
    def __init__(self, name, path):
        super().__init__(name, path)

        self.parse_communication_patterns()
        
    def parse_communication_patterns(self):
        """
        Parse the communication patterns from the node
        """
        with open(self.file_path, 'r') as file:
            file_contents = preProcess(file)

        self.find_publishers(file_contents)
        self.find_subscribers(file_contents)
        self.find_service_servers(file_contents)
        self.find_service_clients(file_contents)
        self.find_action_servers(file_contents)
        self.find_action_clients(file_contents)

    def find_publishers(self, file_contents: str):
        """
        Find the publishers in the node
        """
        search_string = "create_publisher+[(]"

        for match in re.finditer(search_string, file_contents):
            start_index = match.end()
            end_index = findChar(match.string, start_index, ",")
            msg_type = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ",")
            topic_name_raw = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ")")
            qos_profile = match.string[start_index:end_index]

            self.publishers.append(Publisher(msg_type, topic_name_raw, qos_profile))

    def find_subscribers(self, file_contents: str):
        """
        Find the subscribers in the node
        """
        search_string = "create_subscription+[(]"

        for match in re.finditer(search_string, file_contents):
            start_index = match.end()
            end_index = findChar(match.string, start_index, ",")
            msg_type = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ",")
            topic_name_raw = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ",")
            clbk_function = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ")")
            qos_profile = match.string[start_index:end_index]

            self.subscribers.append(Subscriber(msg_type, topic_name_raw, qos_profile))

    def find_service_servers(self, file_contents: str):
        search_string = "create_service+[(]"

        for match in re.finditer(search_string, file_contents):
            start_index = match.end()
            end_index = findChar(match.string, start_index, ",")
            srv_type = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ",")
            srv_name_raw = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ")")
            srv_function = match.string[start_index:end_index]

            self.service_servers.append(ServiceServer(srv_type, srv_name_raw))

    def find_service_clients(self, file_contents: str):
        search_string = "create_client+[(]"
        
        for match in re.finditer(search_string, file_contents):
            start_index = match.end()
            end_index = findChar(match.string, start_index, ",")
            srv_type = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ")")
            srv_name_raw = match.string[start_index:end_index]

            self.service_clients.append(ServiceClient(srv_type, srv_name_raw))

    def find_action_servers(self, file_contents: str):
        search_string = "ActionServer+[(]"

        for match in re.finditer(search_string, file_contents):
            start_index = match.end()
            end_index = findChar(match.string, start_index, ",")
            s = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ",")
            action_type = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ",")
            action_name_raw = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ")")
            action_function = match.string[start_index:end_index]

            self.action_servers.append(ActionServer(action_type, action_name_raw))

    def find_action_clients(self, file_contents: str):
        search_string = "ActionClient+[(]"

        for match in re.finditer(search_string, file_contents):
            start_index = match.end()
            end_index = findChar(match.string, start_index, ",")
            s = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ",")
            action_type = match.string[start_index:end_index]

            start_index = end_index + 1
            end_index = findChar(match.string, start_index, ")")
            action_name_raw = match.string[start_index:end_index]

            self.action_clients.append(ActionClient(action_type, action_name_raw))