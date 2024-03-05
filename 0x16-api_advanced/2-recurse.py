#!/usr/bin/python3
"""use reddit api to print the number of subscribers"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """print the top ten hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "u/Responsible_Peace_80"}
    response = requests.get(
        url, headers=headers, allow_redirects=False, params={"after": after}
    )
    if response.status_code != 200:
        return None
    data = response.json().get("data").get("children")
    after = response.json().get("data").get("after")
    if after is None:
        return hot_list
    for i in data:
        hot_list.append(i.get("data").get("title"))
    return recurse(subreddit, hot_list, after)
