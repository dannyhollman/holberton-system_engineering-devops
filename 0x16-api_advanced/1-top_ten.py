#!/usr/bin/python3
""" returns top 10 posts for subreddit """
import requests


def top_ten(subreddit):
    """ returns top 10 posts """
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {'User-Agent': 'test'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params).json()
    posts = response['data']['children']
    if len(posts) == 0:
        print('None')
    for post in posts:
        print(post['data']['title'])
