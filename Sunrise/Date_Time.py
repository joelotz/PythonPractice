'''
http://stackoverflow.com/questions/4790265/plot-time-of-day-vs-date-in-matplotlib
'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime as dt
import pandas as pd

filename = 'C:\Users\Joe Lotz\Downloads\unnamed-20130108154826.csv'
y = pd.read_csv(filename, sep=',', header=0)

# Make a series of events 1 day apart
x = mpl.dates.drange(dt.datetime(2013,1,1),
                     dt.datetime(2013,12,31),
                     dt.timedelta(days=1))

def getDay(x): return int(x[-2:])
def getMonth(x): return int(x[-5:-3])
def getYear(x): return int(x[:4])
def convertTime(x):
    hour,mins = x.split(':')
    return int(hour)+float(mins)/60

day = map(getDay,y.Date)
month = map(getMonth,y.Date)
year = map(getYear,y.Date)

t = []
for index in range(len(day)):
    t.append(dt.date(year[index],month[index],day[index]))

sunrise = map(convertTime,y.Sunrise)
sunset = map(convertTime,y.Sunset)
daylength = map(convertTime,y.Daylength)

plt.plot(t,sunrise)
plt.plot(t,sunset)
plt.plot(t,daylength)

plt.show()