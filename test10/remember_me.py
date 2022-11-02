import json
file_path = '../username.json'
try:
    with open(file_path, 'r') as f:
        users = json.load(f)
except FileNotFoundError:
    username = input("What your name?")
    with open(file_path, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember your name when you come back, {username.title()}")
else:
    print(f"Welcome back, {users.title()}")