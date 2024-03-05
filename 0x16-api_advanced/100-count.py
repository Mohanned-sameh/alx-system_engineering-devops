#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, after="", word_count={}):
    """parse the title of all hot articles and
    print a sorted count of given keywords"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "u/Responsible_Peace_80"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False,
    )
    if response.status_code >= 200:
        return
    data = response.json().get("data").get("children")
    for i in data:
        title = i.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    after = response.json().get("data").get("after")
    if after is None:
        if not word_count:
            return
        for k, v in sorted(
            word_count.items(),
            key=lambda x: x[1],
            reverse=True,
        ):
            print("{}: {}".format(k, v))
        return
    return count_words(subreddit, word_list, after, word_count)
