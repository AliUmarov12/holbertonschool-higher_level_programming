#!/usr/bin/python3
"""kfnvkfnvin"""

import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.ok:
        json_data = response.json()

        for i in json_data:
            print(i["title"])

def fetch_and_save_posts():
    response = requests.get(url)

    if response.ok:
        json_data = response.json()
        list_of_dicts = [
            {"id": post["id"]
            "title": post["title"]
            "body": post["body"]
             }
            for post in json_data
            ]
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csv_file:
            abc = csv.DictWriter(csv_file, fieldnames=["id", "title", "body"])
            abc.writeheader()
            abc.writerows(list_of_dicts)
