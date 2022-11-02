import json
numbers = [1, 2, 3, 4, 5]
filename = '../number.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
