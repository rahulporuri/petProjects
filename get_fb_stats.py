import numpy
import matplotlib.pyplot as plt
import BeautifulSoup

import time

soup = BeautifulSoup.BeautifulSoup(open('wall.htm'))

allAttrs = [tag.string for tag in soup.findAll('div')]

dates = []
for string in allAttrs:
	try :
		dates.append(str(str(string).strip('u')).split())
	except TypeError :
		print string

#dateList = numpy.asarray(dates, dtype=int)

print len(dates)

dayList = []
dateList = []
monthList = []
yearList = []

for string in dates[3:]:
	try:
		dayList.append(string[0])
		dateList.append(string[2])
		monthList.append(string[1])
		yearList.append(string[3])
	except IndexError:
		print string

#print dayList[:10]
print dict((x, dayList.count(x)) for x in dayList)
print dict((x, dateList.count(x)) for x in dateList)
print dict((x, monthList.count(x)) for x in monthList)
print dict((x, yearList.count(x)) for x in yearList)

plt.hist(dayList, bins=7)
plt.show()
print list(set(dayList))
print list(set([string[1] for string in dates[3:]]))
print list(set([string[2] for string in dates[3:]]))
print list(set([string[3] for string in dates[3:]]))

print yearList
print monthList
print dayList
print dateList

#plt.hist([string[0] for string in dates[3:]], bins=7)
#plt.show()
plt.hist([string[1] for string in dates[3:]], bins=12)
plt.show()
plt.hist([string[2] for string in dates[3:]], bins=31)
plt.show()
plt.hist([string[3] for string in dates[3:]])#,bins=?)
plt.show()
