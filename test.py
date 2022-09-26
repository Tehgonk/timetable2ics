from datetime import datetime, timedelta

start = "2022/09/21 09:30"
# convert to datetime object
start = datetime.strptime(start, "%Y/%m/%d %H:%M")

# create a bool to check if the start time is in daylight savings
is_dst = bool(start.astimezone().utcoffset())

# if true, add '+01:00' to the end of the string, else add '+00:00'
if is_dst:
    start = datetime.strftime(start, "%Y-%m-%d %H:%M:%S+01:00")
else:
    start = datetime.strftime(start, "%Y-%m-%d %H:%M:%S+00:00")

print(start)

# print the current utc offset for london in hours
# print(datetime.now().astimezone().utcoffset().total_seconds() / 3600)

# print the utc offset for start
# print(start.astimezone().utcoffset())