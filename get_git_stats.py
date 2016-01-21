import numpy
import matplotlib.pyplot as plt

import time

dateList = [line.split()[4] for line in open('commit_data.dat')]
dateList = numpy.asarray(dateList, dtype=int)

print len(dateList)

yearList = []
monthList = []
dayList = []
hourList = []

for date in dateList:
	temp = time.gmtime(date)
	yearList.append(temp.tm_year)
	monthList.append(temp.tm_mon)
	dayList.append(temp.tm_mday)
	hourList.append(temp.tm_hour)

yearList = numpy.asarray(yearList)
monthrList = numpy.asarray(monthList)
dayList = numpy.asarray(dayList)
hourList = numpy.asarray(hourList)

print min(yearList), max(yearList)
print list(set(yearList))
print list(set(monthList))
print list(set(dayList))
print list(set(hourList))

plt.hist(yearList)
plt.show()
plt.hist(monthList,bins=12)
plt.show()
plt.hist(dayList,bins=31)
plt.show()
plt.hist(hourList,bins=24)
plt.show()
