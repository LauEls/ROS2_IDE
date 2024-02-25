import re
import os
from package import Package
from py_node import PythonNode
from parse_util import findChar, preProcess

class PythonPackage(Package):
    def __init__(self, path):
        super().__init__(path)

        self.file_path = os.path.join(self.path, "setup.py")

        self.name = self.parse_package_name()
        self.nodes = self.parse_nodes()

    def parse_package_name(self):
        """
        Parse the package name from the setup.py file
        """
        search_string = "package_name"
        
        with open(self.file_path, 'r') as file:
            file_contents = preProcess(file)
            match = re.search(search_string, file_contents)

        if match is None:
            print("Package Name not found!")
            return None

        name_start = findChar(match.string, match.end(), "'") + 1
        name_end = findChar(match.string, name_start, "'")

        print("Package Name: ", match.string[name_start:name_end])
        return match.string[name_start:name_end]

    def parse_nodes(self):
        """
        Parse the nodes from the setup.py file
        """
        search_string = self.name
        node_names = []
        
        with open(self.file_path, 'r') as file:
            # file_contents = file.read()
            file_contents = preProcess(file)
            for match in re.finditer(search_string, file_contents):
                if match.string[match.end()] == ".":
                    start_index = match.end() + 1
                    i = start_index
                    while match.string[i] != ":":
                        i += 1

                    end_index = i
                    # print("Node found: ", match.string[start_index:end_index])
                    node_names.append(match.string[start_index:end_index])

        walk_dir = os.path.join(self.path, self.name)
        # print('Node Directory = ' + walk_dir)
        nodes = []
        for root, subdirs, files in os.walk(walk_dir):
            for file in files:
                for node_name in node_names:
                    if file == node_name + ".py":
                        # print("node file: ", file)
                        print("Node: ", node_name)

                        new_node = PythonNode(node_name, os.path.join(root, file))
                        nodes.append(new_node)
                        break

                    
                    
        return nodes
        
        