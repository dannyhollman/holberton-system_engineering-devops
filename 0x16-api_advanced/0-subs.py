#!/usr/bin/python3
""" returns subscriber counter for subreddit """
import requests


def number_of_subscribers(subreddit):
    """ returns subscriber count """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'test'}).json()
    try:
        return response['data']['subscribers']
    except:
        return 0
