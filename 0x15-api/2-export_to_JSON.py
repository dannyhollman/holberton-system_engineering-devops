#!/usr/bin/python3
""" returns TODO list from API """
import csv
import json
import requests
from sys import argv


def main():
    """ returns TODO list """
    total = 0
    complete = 0
    user_url = "https://jsonplaceholder.typicode.com/users/"
    task_url = "https://jsonplaceholder.typicode.com/todos?userId="
    user = requests.get('{}{}'.format(user_url, argv[1])).json()
    tasks = requests.get('{}{}'.format(task_url, argv[1])).json()

    for task in tasks:
        task['username'] = user['username']
        task['task'] = task['title']
        del task['title']
        del task['id']
        del task['userId']

    with open("{}.json".format(argv[1]), "w") as f:
        json.dump({argv[1]: tasks}, f)

if __name__ == "__main__":
    main()
