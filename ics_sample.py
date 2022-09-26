from datetime import datetime, timedelta
from ics import Calendar, Event

c = Calendar()
e = Event()
e.summary = "My cool event"
e.description = "A meaningful description"
e.begin = '2022-09-21 11:15:00+01:00'
e.end = '2022-09-21 12:15:00+01:00'
c.events.add(e)

with open("sample.ics", "w") as f:
    f.write(c.serialize())