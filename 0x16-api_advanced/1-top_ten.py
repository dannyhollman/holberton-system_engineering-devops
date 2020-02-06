#!/usr/bin/python3
""" returns top 10 posts for subreddit """
import requests
from sys import argv


def top_ten(arg):
    """ returns top 10 posts """
    url = "http://www.reddit.com/r/{}/hot.json?limit=10".format(arg)
    headers = {'User-Agent': 'test'}
    response = requests.get(url, headers=headers).json()
    posts = response['data']['children']
    if len(posts) == 0:
        print('None')
    for post in posts:
        print(post['data']['title'])


if __name__ == "__main__":
    top_ten()
