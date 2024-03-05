#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Function to return the number of subscribers"""
    sub_info = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(),
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False,
    )
    if sub_info.status_code != 200:
        return 0
    return sub_info.json().get("data").get("subscribers")
