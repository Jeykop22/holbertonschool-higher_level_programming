#!/usr/bin/python3
"""
    Script that adds all arguments to a Python list,
    and then save them to a file
"""
from sys import argv
from pathlib import Path
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"

if Path(file).exists():
    my_list = load(file)
else:
    my_list = []

for arg in range(1, len(argv)):
    my_list.append(argv[arg])
save(my_list, file)
