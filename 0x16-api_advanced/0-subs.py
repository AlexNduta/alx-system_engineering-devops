#!/usr/bin/python3
""" -queries the Reddit API and return total subs of each subreddit
    -if an invalid subredit is given, return 0
"""
import requests
import sys

def number_of_subscribers(subreddit):
    """ return number of subscribers in a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    rq = requests.get(url).json()
    subscribers = rq.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers

if __name__ == '__main__':
    result = number_of_subscribers(sys.argv[1])
    print(result)
