#!/usr/bin/python3
""" returns TODO list from API """
import csv
import json
import requests


def main():
    """ returns TODO list """
    user_url = "https://jsonplaceholder.typicode.com/users"
    task_url = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(user_url).json()
    tasks = requests.get(task_url).json()

    final = {}

    for user in users:
        temp = []
        for task in tasks:
            dic = dict(task)
            if dic['userId'] == user['id']:
                dic['username'] = user['name']
                dic['task'] = dic['title']
                del dic['title']
                del dic['id']
                del dic['userId']
                temp.append(dic)
        final[user['id']] = temp

    with open('todo_all_employees.json', 'w') as f:
        json.dump(final, f)

if __name__ == "__main__":
    main()
