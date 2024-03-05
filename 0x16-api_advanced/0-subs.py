#!/usr/bin/python3
def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
