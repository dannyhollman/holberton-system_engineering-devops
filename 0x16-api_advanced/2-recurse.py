#!/usr/bin/python3
""" returns list of hot posts for subreddit """
import requests
from sys import argv


def recurse(arg, hot_list=[], count=0):
    """ returns list of hot posts """
    url = "http://www.reddit.com/r/{}/hot.json".format(arg)
    headers = {'User-Agent': 'test'}
    response = requests.get(url, headers=headers).json()
    posts = response['data']['children']
    if count == len(posts) - 1:
        return hot_list
    hot_list.append(posts[count]['data']['title'])
    return recurse(arg, hot_list, count + 1)


if __name__ == "__main__":
    recurse(argv[1])
