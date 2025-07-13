# naive and aware datetimes

# naive dates and times dont have timezone info or daylight savings times
# aware dates and times have timezonne info and keep track of daylight savings time

import datetime

d = datetime.date(2025, 1, 27) #datetime.date works with year, month and day
print(d)

# to get today's local date

today = datetime.date.today()
print(today)
print(today.year)
print(today.weekday()) # Have monday as 0 and sunday as 6
print(today.isoweekday()) # Have monday as 1 and sunday as 7

# time delta
print(datetime.datetime.now()) # returns datetime object containing current local date and time

sevenDaysAgo = datetime.datetime.now() - datetime.timedelta(days = 7)
print(sevenDaysAgo)

# get date 7 days from today
sevenDaysLaterDate = today  + datetime.timedelta(days=7)
print(sevenDaysLaterDate)

# to get date 2 days ago
twoDaysAgoDate = today - datetime.timedelta(days=2)
print(twoDaysAgoDate)

# subtracting two dates return time delta
bday=datetime.date(2025, 1 ,27)
timePassedSinceBday = today - bday
print(timePassedSinceBday)

# datetime.time works with hours, minutes, seconds, microseconds
# datetime.time follows 24 hr format by default, so  we can pass hours from 0 to 23 
t=datetime.time(15,23,14,7)
print(t)
print(t.hour)

# to get both date and time, we use datetime.datetime()

dt = datetime.datetime(2012,5,1,23,45,59)
print(dt)
print(dt.date())
print(dt.time())
print(dt.month)

# datetime with time delta
curDateTime = datetime.datetime.now()
twelevHoursLater = curDateTime + datetime.timedelta(hours=12)
print(twelevHoursLater)

# dt_today returns current local  datetime without any timezone
dt_today = datetime.datetime.today()
print(dt_today)

# dt_now returns current local datetime with option to pass in timezone
dt_now = datetime.datetime.now()
print(dt_now)

# dt_utcnow returns current utc datetime
dt_utcnow = datetime.datetime.now()
print(dt_utcnow)
print(dt_utcnow.tzinfo)

# to work with timezones, we use a package called pytz