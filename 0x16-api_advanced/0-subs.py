#!/usr/bin/python3
"""use reddit api to print the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """print the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "u/Responsible_Peace_80"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    return response.json().get("data").get("subscribers")
