import json

file_path = '../number.json'

with open(file_path, 'r') as f:
    numbers = json.load(f)
print(numbers)