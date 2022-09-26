from ics import Calendar, Event
from datetime import datetime
import json

def utc_offset(event_time):
    """ Convert datetime parameter to a datetime object, then check if a dst offset
        needs to added. If true, add '+01:00' to the end of the string, else add '+00:00' """

    # convert to datetime object  
    datetime_obj = datetime.strptime(event_time, "%Y/%m/%d %H:%M")
    # create a bool to check if the start time is in daylight savings
    if bool(datetime_obj.astimezone().utcoffset()):
        return datetime.strftime(datetime_obj, "%Y-%m-%d %H:%M:%S+01:00")
    else:
        return datetime.strftime(datetime_obj, "%Y-%m-%d %H:%M:%S+00:00")

c = Calendar()

with open('clean_data.json') as json_file:
    data = json.load(json_file)
    for item in data['appointments']:
        e = Event()
        e.name = item['subject']
        e.location = item['description'].split(' ')[0]
        e.begin = utc_offset(item['start'])
        e.end = utc_offset(item['end'])
        c.events.add(e)

with open("my.ics", "w") as f:
    # f.writelines(c)
    f.write(c.serialize())