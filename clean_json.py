import json


# with open('data.json', encoding='utf-8') as json_file:
#     data = json.load(json_file)

with open('clean_data.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

# dump the edited json data to a file
with open('clean_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)