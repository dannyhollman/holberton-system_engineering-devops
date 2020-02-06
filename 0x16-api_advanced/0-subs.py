#!/usr/bin/python3
""" returns subscriber counter for subreddit """
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ returns subscriber count """
    url = "http://www.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'test'}).json()
    try:
        return response['data']['subscribers']
    except:
        return 0

if __name__ == "__main__":
    number_of_subscribers()
