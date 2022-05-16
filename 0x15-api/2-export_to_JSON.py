#!/usr/bin/python3
"""
Gather data from an API
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv
from package.fprint import fprint

# Data
ID = argv[1]
url_api = "https://jsonplaceholder.typicode.com"

# Endpoints
ep_user = "{}/users/{}".format(url_api, str(ID))
ep_todos = "{}/todos".format(ep_user)

# Requests
user = requests.get(ep_user)
todos = requests.get(ep_todos)

# Format
user = user.json()
todos = todos.json()

# Output
json_to_export = {}
json_to_export[ID] = []
with open(str(ID) + ".json", "w", encoding="utf8") as file:
    for task in todos:
        json_to_export[ID].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })
    fprint(json_to_export)
    json.dump(json_to_export, file)
