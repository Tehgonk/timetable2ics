from datetime import datetime
import json


with open('clean_data.json') as json_file:
    data = json.load(json_file)

for item in reversed(data['appointments']):
    item['subject'] = item['subject'].replace('\\u003cbr', '').replace('\\u003e', '').replace(' /', ' w/ ')
    item['description'] = item['description'].replace('(', '').replace(')', '')
    
# dump to json file
with open('clean_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)