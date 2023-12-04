from os import path
from sys import path as sys_path
sys_path.insert(0, path.abspath(path.join(path.dirname(__file__), '..')))

import src
