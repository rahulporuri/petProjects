
# coding: utf-8

# If you came here from the blog part of my website, you can go back to it by clicking [here](http://rahulporuri.github.io/blog.html) or if you came here from my blogpost, you can go back to it by clicking [here](http://rahulporuri.blogspot.in/).

# I wanted to look at my commit stats on Github. While Github itself 
# displays the number of commits I've done, I wanted to try it myself. 
# In the process, learn something maybe.

# In order to look at the stats, we first need to put them all in the same 
# file. We can run the following command to create a file with the relevant 
# information, which we can parse using Python later in the code. If you are 
# not working on IPython, you can run the same command without the exclamation 
# point on the terminal. Also, I store all of my Github repositories in the 
# home directory, ~, under a directory 'Github'. The * will look through all sub-
# directories for the file we want.

# In[1]:

get_ipython().system(u'more ~/Github/*/.git/logs/HEAD > commit_data.dat')


# we need the time Python module because we get timestamps in the form of a 10-digit 
# number, which we then need to convert into a date-time format we can understand.

# In[2]:

import numpy
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import time


# We cant run these commands because if you look at the file we just created, 
# you will notice lines containing information on the directory from which the 
# messages were added, which we ofcourse don't need.
# '''
# dateList = [line.split()[4] for line in open('commit_data.dat')]
# dateList = numpy.asarray(dateList, dtype=int)
# print len(dateList)
# '''

# In[3]:

dateList = []
for line in open('commit_data_temp.dat'):
    try:
        dateList.append(line.split()[4])
    except IndexError:
        print line
        
dateList = numpy.asarray(dateList, dtype=int)
print len(dateList)


# time.gmtime(foo) will convert the 10-digit timestamp into a format 
# that we can understand, as I had mentioned earlier. You can look 
# at the following example to understand it better.

# In[10]:

time.gmtime(1452664187)


# In[4]:

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


# I do list(set(fooList)) because I want to confirm that we have 
# meaningful dates. It has happened that a few months of the year 
# or days of the week were missing in a different dataset.

# In[5]:

print min(yearList), max(yearList)
print list(set(yearList))
print list(set(monthList))
print list(set(dayList))
print list(set(hourList))


# In[6]:

plt.hist(yearList, bins=3)


# In[7]:

plt.hist(monthList,bins= 12)


# In[8]:

plt.hist(dayList, bins=31)


# note that the following plot needs to be shifted right by 
# +0530 because I didn't bother doing so myself. The time stamps 
# were with respect to UTC and not local time.

# In[9]:

plt.hist(hourList, bins=24)


# If you came here from the blog part of my website, you can go back to it by clicking [here](http://rahulporuri.github.io/blog.html) or if you came here from my blogpost, you can go back to it by clicking [here](http://rahulporuri.blogspot.in/).

# In[ ]:



