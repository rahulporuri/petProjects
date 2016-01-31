# http://arxiv.org/help/api/examples/python_arXiv_parsing_example.txt
# http://arxiv.org/help/api/index#python_simple_example
# http://arxiv.org/help/api/user-manual
# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html#Parsing XML

import urllib
from BeautifulSoup import BeautifulStoneSoup

url = 'http://export.arxiv.org/api/query?search_query=all:astro&start=0&max_results=1000'
data = urllib.urlopen(url).read()
soup = BeautifulStoneSoup(data)

#print(soup.prettify())
'''
list = soup.findAll('arxiv:affiliation')
for i in range(len(list)):
	print list[i].contents
'''

#test = [tag.string for tag in soup.findAll('arxiv:aiffiliation')]
test = [tag for tag in soup.findAll('entry')]

affiliationList = []
for i in range(len(test)):
	if test[i].findAll('arxiv:affiliation') != []:
		affiliationList.append([tag.string for tag in test[i].findAll('arxiv:affiliation')])

#print affiliationList
#print len(affiliationList)

for temp in affiliationList:
	for temptemp in temp:
		print temptemp.strip('u')
	print '\n'

'''
import feedparser
feed = feedparser.parse(data)

for entry in feed.entries:
	author_string = entry.author
	try:
		author_string += ' (%s)' %entry.arxiv_affiliation
	except AttributeError:
		pass

	print 'Last Author: %s'%author_string
'''
