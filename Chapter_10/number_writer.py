import json

numbers = [2, 3, 5, 7, 11, 13]

filepath = 'text_files/numbers.json'
with open(filepath, 'w') as f:
    json.dump(numbers, f)