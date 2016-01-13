'''
http://stackoverflow.com/questions/7141431/python-extracting-html-tag-attributes-without-regular-expressions
https://docs.python.org/2/library/htmlparser.html
http://www.crummy.com/software/BeautifulSoup/bs4/doc/

http://stackoverflow.com/questions/539900/google-bookmark-export-date-format

html_doc = open('bookmarks.html')
soup = BeautifulSoup(html_doc)

j = 0
for link in soup.find_all('a'):
	j += 1


dates = np.zeros(j)
j = 0

for link in soup.find_all('a'):
	dates[j] = link.get('add_date')
	j += 1

print j
print len(dates)
print np.min(dates), np.max(dates)

plt.hist(dates,50)
plt.show()
'''

import numpy
import matplotlib.pyplot as plt
import BeautifulSoup

import time

soup = BeautifulSoup.BeautifulSoup(open('ril_export.html'))

allAttrs = [tag.attrs for tag in soup.findAll('a')]

dates = []
for string in allAttrs:
	try :
		dates.append(str(string[1][1]).strip('u'))
	except IndexError :
		print string

dateList = numpy.asarray(dates, dtype=int)

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


plt.hist(yearList,bins=2)
plt.show()
plt.hist(monthList,bins=12)
plt.show()
plt.hist(dayList,bins=31)
plt.show()
plt.hist(hourList,bins=24)
plt.show()
