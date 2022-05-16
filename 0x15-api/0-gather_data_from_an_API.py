#!/usr/bin/python3
"""
    Gather data from an API
"""


if __name__ == "__main__":
    import json
    from sys import argv
    from urllib import request as rq

    employeeID = argv[1]
    user_bio = {}
    todo_list = []
    done_tasks = []
    _url_1 = 'https://jsonplaceholder.typicode.com/users'
    _url_2 = 'https://jsonplaceholder.typicode.com/todos'
    with rq.urlopen('{}/{}'.format(_url_1, employeeID)) as urlObj:
        user_bio = json.loads(urlObj.read())

    with rq.urlopen(_url_2) as urlObj:
        response = json.loads(urlObj.read())
        for r in response:
            if r.get('userId') == int(employeeID):
                todo_list.append(r)
                if r.get('completed') is True:
                    done_tasks.append(r)

    print("Employee {} is done with tasks({}/{}):".format(
        user_bio.get('name'), len(done_tasks), len(todo_list)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
