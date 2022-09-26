from ics import Calendar, Event
from datetime import datetime, timedelta
import json

def utc_offset(event_time):
    """ Convert datetime parameter to a datetime object, then check if a dst offset
        needs to be added. If true, add '+01:00' to the end of the string, else add '+00:00' """

    # convert to datetime object  
    datetime_obj = datetime.strptime(event_time, "%Y/%m/%d %H:%M")

    # create a bool to check if the start time is in daylight savings
    if bool(datetime_obj.astimezone().utcoffset()):
        return datetime.strftime(datetime_obj, "%Y-%m-%d %H:%M:%S+01:00")
    else:
        return datetime.strftime(datetime_obj, "%Y-%m-%d %H:%M:%S+00:00")

# opend the combined.ics file
with open("combined.ics", "r") as f:
    c = Calendar(f.read())

with open('clean_data.json') as json_file:
    data = json.load(json_file)
    for item in data['appointments']:

        # Set the event properties
        e = Event()
        e.name = item['subject']
        e.location = item['description'].split(' ')[0]
        e.begin = utc_offset(item['start'])
        e.end = utc_offset(item['end'])

        # add event to the calendar
        c.events.add(e)

# append to 'combined.ics'
with open("combined.ics", "w") as f:
    f.write(c.serialize())