import os
import sys
from py_package import PythonPackage

walk_dir = '/home/laurenz/phd_project/ros2_gh360_ws/src'

#print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
#print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

packages = []

for root, subdirs, files in os.walk(walk_dir):
    for file in files:
        if file == "setup.py":
            new_package = PythonPackage(root)
            packages.append(new_package)
        
        if file == "CMakeLists.txt":
            pass