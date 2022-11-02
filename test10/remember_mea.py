import json

remember_name = input("Please tell me your name:\n")
file_path = '../username.json'
with open(file_path, 'w') as f:
    json.dump(remember_name, f)
    print(f"We'll remember your name when you come back, {remember_name.title()}")