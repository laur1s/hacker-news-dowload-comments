import requests
import json
import csv
import sys


url = "https://hacker-news.firebaseio.com/v0/item/" + str(sys.argv[1]) + ".json"

try:
    r = requests.get(url)
    story = r.json()
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)


if story is None:
    print("Story with the following ID doesn't exist")
    sys.exit(1)

with open("comment.csv", "w", newline="") as csvfile:
    fieldnames = ["id", "text"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

for comment in story["kids"]:
    try:
        r = requests.get(
            "https://hacker-news.firebaseio.com/v0/item/" + str(comment) + ".json"
        )
        it = r.json()
    except requests.exceptions.RequestException as e:
        print(e)
    if it is not None and "text" in it:
        with open("comments.csv", "a", newline="") as csvfile:
            fieldnames = ["id", "text"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": it["id"], "text": it["text"]})
