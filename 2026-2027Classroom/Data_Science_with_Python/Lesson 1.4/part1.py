#Import the datatime module
import datetime as dt

#Continue with the tasks here
# print today's date
today = dt.date.today()
print(today)
print()

# print today's time now
now = dt.datetime.now()
print(now)
print()
# Challenge
for i in range(8):
    future = today + dt.timedelta(days=i)
    print(future)
    i += 1

from math import sqrt
print(sqrt(16))