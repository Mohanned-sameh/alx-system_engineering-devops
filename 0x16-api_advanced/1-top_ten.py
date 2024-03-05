#!/usr/bin/python3
"""use reddit api to print the top ten hot posts"""
import requests


def top_ten(subreddit):
    """print the top ten hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "u/Responsible_Peace_80"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 200:
        print("None")
        return
    data = response.json().get("data").get("children")
    for i in data:
        print(i.get("data").get("title"))
    return
