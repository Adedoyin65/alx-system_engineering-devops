#!/usr/bin/python3

"""
This recursive function queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of all hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles
        of hot articles. Defaults to an empty list.

    Returns:
        list: A list containing the titles of all hot
        articles for the given subreddit, or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My Reddit API Client'}
    try:
        response = requests.get(url, headers=headers, params={limit: 100}, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if not data[data][children]:
                return hot_list
            else:
                for post in data[data][children]:
                    hot_list.append(post[data][title])
                last_post = data[data][children][-1][data][name]
                return recurse(subreddit, hot_list, params={after: last_post})
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
