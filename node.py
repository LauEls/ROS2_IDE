

class Node:
    def __init__(self, name, path):
        self.file_path = path
        self.node_name = name
        self.publishers = []
        self.subscribers = []
        self.service_servers = []
        self.service_clients = []
        self.action_servers = []
        self.action_clients = []
             