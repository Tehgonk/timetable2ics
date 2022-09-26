from datetime import datetime

start = "2022/09/21 09:30"
end = "2022/09/21 11:15"

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


print(utc_offset(start))
print(utc_offset(end))