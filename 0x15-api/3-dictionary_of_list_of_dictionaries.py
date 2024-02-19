#!/usr/bin/python3
""" Export data in the JSON format """
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    user_dict = {}
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        for task in todos:
            user_dict[user_id].append(
                {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
            )
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_dict, jsonfile)
