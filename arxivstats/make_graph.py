import json
from collections import defaultdict
from graphcanvas.api import GraphView, graph_from_dict

import urllib
from BeautifulSoup import BeautifulStoneSoup

url = 'http://export.arxiv.org/api/query?search_query=all:astro&start=0&max_results=500'
data = urllib.urlopen(url).read()
soup = BeautifulStoneSoup(data)

test = [tag for tag in soup.findAll('entry')]

affiliationList = []
for i in range(len(test)):
            if test[i].findAll('arxiv:affiliation') != []:
                                affiliationList.append([tag.string for tag in test[i].findAll('arxiv:affiliation')])

testDict = defaultdict(dict)
for alist in affiliationList:
    for what in alist:
        if len(testDict[what]) == 0:
            testDict[what] = []
        for item in alist:
            if item != what:
                testDict[what].append(item)

#GraphView(graph=graph_from_dict(json.load(open('arxiv_data.dat')))).configure_traits()
GraphView(graph=graph_from_dict(testDict)).configure_traits()
