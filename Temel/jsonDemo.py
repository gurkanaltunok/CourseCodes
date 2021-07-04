import json

with open("users.json") as users:
    data = json.load(users)

    for u in range(5):
        print(data[u]["username"])
        print(data[u]["email"])
        print(data[u]["address"]["street"])
        print(data[u]["address"]["geo"]["lat"])
