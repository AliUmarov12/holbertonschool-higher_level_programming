#!/usr/bin/python3
"""
This script adds all command line arguments to a list and saves them to a JSON file.
"""
import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
items = []

if Path(filename).exists():
    items = load_from_json_file(filename)

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
