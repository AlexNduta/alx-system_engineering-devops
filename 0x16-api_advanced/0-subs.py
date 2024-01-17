#!/usr/bin/python3
""" -queries the Reddit API and return total subs of each subreddit
    -if an invalid subredit is given, return 0
"""
import requests
def number_of_subscribers(subreddit):
    """ return number of subscribers in a given subreddit"""
    url="https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    rq = requests.get(url).json()
    subscriber = rq.get('data', {}).get('subscriber')
    if not subscriber:
        return 0
    return subscriber

