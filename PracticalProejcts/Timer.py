# Created on Mon Mar 23 09:45:09 2020

# @author: Nata

import datetime as dt

import time 

start = int(input(' how many seconds should the timer be?'))

# A timedelta object represents a duration, the difference between two dates or times.

# class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
# All arguments are optional and default to 0. Arguments may be ints,
#  longs, or floats, and may be positive or negative

count = dt.timedelta(seconds=start)

while start != 0 :
    count = count - dt.timedelta(seconds =1)
    # Pauses program for one second
    
    time.sleep(1)
    start = start -1
    print(start)
    print(dt.now())
else:   
    print("time is up")