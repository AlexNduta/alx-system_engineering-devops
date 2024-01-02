#!/usr/bin/python3
"""
    ->consumes the RESTAPI for a given emplyee ID
    returns info about his/her TODO list progress
    ->
"""
import requests
import sys

ID = sys.argv[1]
url = requests.get("https://jsonplaceholder.typicode.com/todos/{}".format(ID))

print(url.json())

