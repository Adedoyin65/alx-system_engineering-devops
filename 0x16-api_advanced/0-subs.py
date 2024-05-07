#!/usr/bin/python3
"""A module that sends a http request to reddit api"""
import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers for a given subreddit.

        Args:
           subreddit (str): The name of the subreddit.

        Returns:
           int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': "My Reddit API Client"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
