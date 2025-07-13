import datetime
import pytz

dt = datetime.datetime(2014,12,1,23,1,tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# to view all timezones available in pytz
for tz in pytz.all_timezones:
    print(tz)

# to convert the dt_utcnow in another timezone
dt_indianow=dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_indianow)

# to convert naive time as timezone aware
dt_local = datetime.datetime.now() # naive datetime
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_local)
print(dt_mtn)  # aware datetime

# convert one timezone to another
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

# print datetime in iso format
print(dt_east.isoformat())

# format datetime
print(dt_east.strftime('%B %d, %Y'))
# Refer to https://docs.python.org/3/library/datetime.html - Format Codes for formatting codes

# convert datetime string to datetime object
dt_str = "July 13, 2025"
dt_obj = datetime.datetime.strptime(dt_str, '%B %d, %Y') # second argument is the current format of passed datetime string
print(dt_obj)