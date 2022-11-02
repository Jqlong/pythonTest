import json
file_path = '../username.json'
with open(file_path, 'r') as f:
    users = json.load(f)
    print(f"Welcome back, {users.title()}")
