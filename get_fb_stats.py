
# coding: utf-8

# If you came here from the blog part of my website, you can go back to it by clicking [here](http://rahulporuri.github.io/blog.html) or if you came here from my blogpost, you can go back to it by clicking [here](http://rahulporuri.blogspot.in/).

# A long, long time back, I had downloaded a copy of my facebook data, which included information on all the posts I had written over the years, all of the comments I'd written and things I liked. More recently, similar to the other pet projects I am working on, I wanted to look at basic statistics of my activity on facebook. If you want to do the same, go [here](https://www.facebook.com/settings) and click on "Download a copy of your Facebook data". Once you've downloaded it, you will find a .htm file titled 'wall.htm'. Again, if you don't have IPython, you can run the python code that can be found [here](https://github.com/rahulporuri/peepees/blob/master/get_fb_stats.py)

# I use the BeautifulSoup module to parse the .htm file.

# In[1]:

import numpy
import BeautifulSoup
import time


# if you look at the 'wall.htm' file, you will understand the structure and where the timestamps pertaining to posts, comments and whatnot are. They are the 'string' attribute of the 'div' elements in the htm file.

# In[2]:

soup = BeautifulSoup.BeautifulSoup(open('wall.htm'))
allAttrs = [[tag.attrs, tag.string] for tag in soup.findAll('div')]


# the attribute u'meta' corresponds to the timestamps of any and every activity on my wall. the attribute u'comment' corresponds to comments. Blindly getting tag.string values will add noise to our timestamp dataset so we check to make sure that the attribute is meta before we add the string/timestamp.

# In[3]:

dates = []
for string in allAttrs:
    try :
        if string[0][0][1] == u'meta':
            try :
                dates.append(str(str(string[1]).strip('u')).split())
            except TypeError :
                print string
    except IndexError:
        pass

#dateList = numpy.asarray(dates, dtype=int)

print len(dates)


# how the string/time stamps look

# In[4]:

dates[:10]


# In[5]:

dayList = []
dateList = []
monthList = []
yearList = []

for string in dates:
        try:
                dayList.append(string[0])
                dateList.append(string[2])
                monthList.append(string[1])
                yearList.append(string[3])
        except IndexError:
                print string                


# from the numerous lists, we create a dictionary that tells us how many of each day/date/month/year are present in the list.

# In[6]:

dayListDict = dict((x, dayList.count(x)) for x in dayList)
dateListDict = dict((x, dateList.count(x)) for x in dateList)
monthListDict = dict((x, monthList.count(x)) for x in monthList)
yearListDict = dict((x, yearList.count(x)) for x in yearList)


# In[7]:

print dayListDict


# In[8]:

print dayListDict['Monday,'], dayListDict['Tuesday,'], dayListDict['Wednesday,']
print dayListDict['Thursday,'], dayListDict['Friday,'], dayListDict['Saturday,'], dayListDict['Sunday,']


# In[9]:

print monthListDict


# In[10]:

print monthListDict['January'], monthListDict['February'], monthListDict['March'], monthListDict['April']
print monthListDict['May'], monthListDict['June'], monthListDict['July'], monthListDict['August']
print monthListDict['September'], monthListDict['October'], monthListDict['November'], monthListDict['December']


# In[11]:

print yearListDict


# In[12]:

print yearListDict['2009'], yearListDict['2010'], yearListDict['2011'], yearListDict['2012']
print yearListDict['2013'], yearListDict['2014'], yearListDict['2015']


# In[13]:

print dateListDict


# If you came here from the blog part of my website, you can go back to it by clicking [here](http://rahulporuri.github.io/blog.html) or if you came here from my blogpost, you can go back to it by clicking [here](http://rahulporuri.blogspot.in/).
