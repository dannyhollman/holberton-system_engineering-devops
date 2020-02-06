#!/usr/bin/python3
""" returns subscriber counter for subreddit """
import requests
from sys import argv


def number_of_subscribers(arg):
    """ returns subscriber count """
    url = "http://www.reddit.com/r/{}/about.json".format(arg)
    response = requests.get(url, headers={'User-Agent': 'test'}).json()
    for k, v in response.items():
        if k == "data":
            try:
                return v['subscribers']
            except:
                return 0

if __name__ == "__main__":
    number_of_subscribers()
