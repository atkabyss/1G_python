import json

json_file = open('python.json', encoding='utf-8')
json_data = json.load(json_file)

for order in json_data["Items"]:
    print(order["Item"]["title"])



