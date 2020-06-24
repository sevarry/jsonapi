#!/usr/bin/env python

import json
import time
import datetime
import requests


class challenger:
    def get_post(self, post_id):
        return requests.get(
            'https://jsonplaceholder.typicode.com/posts/{:d}/'.format(post_id))

    def add_post(self, title, user_id, body):
        return requests.post(
            'https://jsonplaceholder.typicode.com/posts/',
            json={'Title': title, 'UserID': user_id, 'Body': body})

    def del_post(self, post_id):
        return requests.delete(
            'https://jsonplaceholder.typicode.com/posts/{:d}/'.format(post_id))

# Task 1
c = challenger()
post_id = 99
r = c.get_post(post_id)
data = r.json()
print()
print(data['title'])
print()

# Task 2
post_id = 100
r = c.get_post(post_id)
ts = time.time()
utc = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
t = {'time': utc}
data = r.json()
data.update(t)
print(data)
print()

# Task 3
title = 'Testing Some Things'
user_id = '500'
body = 'This is an insertion test with a known API'
r = c.add_post(title, user_id, body)

# Task 4
if r.status_code != 201:
    print('Task three failed: {}'.format(r.status_code))
else:
    data = r.json()
    results = ((data['id']), r.status_code, (r.headers['x-Powered-By']))

# Task 5
print(results)

# Task 6
post_id = data['id']
r = c.del_post(post_id)
print()
print(r.status_code)
print(r.headers['x-content-type-options'])

