import datetime
from datetime import date
# from datetime import datetime
import pytz
from datetime import timedelta
# from datetime import datetime, date


# python datetime module
# Python has a datetime for dates and times
"""Task1:Get current date and time """
# We then used the now() method to create a datetime
# object containing the current local date and time.
now = datetime.datetime.now()
print(now)

""" Task2:Get current Date"""
# we have used the today() method defined in the date
# class to get a date object containing the current local date.

current_date = datetime.date.today()
print(current_date)

"""Task3:"""

# python datetime.date class
# date object to represent a date
# Here, date() in the above example is a constructor of the date class.
# The constructor takes three arguments: year, month and day
d = datetime.date(2023, 7, 17)
print(d)

d = date(2023, 7, 17)
print(d)

# Get current date using date()
# We can create a date object containing the current date by using the class method named today()

# today() to get current date
todays_date = date.today()

print("Today's date =", todays_date)

"""Task 4:Get date from a timestamp"""

timestamp = date.fromtimestamp(1336244364)
print("Date =", timestamp)

"""Task 5: Get today's year,month and day'"""

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# Handling timezones in Python
# will use pytz module for handling different timezones in different countries

local = datetime.datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

# Time duration in seconds

# t = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
# print("Total seconds =", t.total_seconds())
#
# # Difference between two delta time objects
#
# t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
# t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
#
# t3 = t1 - t2
#
# print("t3 =", t3)
#
# # Python datetime.timedelta Class
# # A timedelta objects represents two different between two dates or times
#
#
# # using date()
# t1 = date(year=2018, month=7, day=12)
# t2 = date(year=2017, month=12, day=23)
#
# t3 = t1 - t2
#
# print("t3 =", t3)
#
# # using datetime()
# t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
# t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
# t6 = t4 - t5
# print("t6 =", t6)
#
# print("Type of t3 =", type(t3))
# print("Type of t6 =", type(t6))

#if one wants to get all the timezones
for timezone in pytz.all_timezones:
    print(timezone)