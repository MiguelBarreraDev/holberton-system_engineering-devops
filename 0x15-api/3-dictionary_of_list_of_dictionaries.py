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
url_api = "https://jsonplaceholder.typicode.com"

# Endpoints
ep_users = "{}/users".format(url_api)

# Requests
users = requests.get(ep_users)

# Format
users = users.json()

# Output
json_to_export = {}
with open("todo_all_employees.json", "w", encoding="utf8") as file:
    for user in users:
        json_to_export[user.get("id")] = []
        ep_user_todos = "{}/{}/todos".format(ep_users, user.get("id"))
        todos = requests.get(ep_user_todos).json()
        for task in todos:
            json_to_export[user.get("id")].append({
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            })
    fprint(json_to_export)
    json.dump(json_to_export, file)
