#!/usr/bin/python3
""" returns TODO list from API """
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
        if task['completed'] is True:
            complete += 1
        total += 1
    print("Employee {} is done with tasks({}/{}):".format(user['name'],
          complete, total))
    for task in tasks:
        if task['completed'] is True:
            print("\t {}".format(task['title']))

if __name__ == "__main__":
    main()
