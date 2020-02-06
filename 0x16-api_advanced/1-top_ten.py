#!/usr/bin/python3
""" returns top 10 posts for subreddit """
import requests


def top_ten(subreddit):
    """ returns top 10 posts """
    url = "http://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'test'}
    response = requests.get(url, headers=headers).json()
    posts = response['data']['children']
    if len(posts) == 0:
        print('None')
    for post in posts:
        print(post['data']['title'])
