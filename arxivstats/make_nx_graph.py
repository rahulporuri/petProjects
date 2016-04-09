import json
from collections import defaultdict
from graphcanvas.api import GraphView, graph_from_dict
import networkx as nx
import matplotlib.pyplot as plt

import urllib
from BeautifulSoup import BeautifulStoneSoup

url = 'http://export.arxiv.org/api/query?search_query=all:astro&start=0&max_results=1000'
data = urllib.urlopen(url).read()
soup = BeautifulStoneSoup(data)

test = [tag for tag in soup.findAll('entry')]

affiliationList = []
for i in range(len(test)):
            if test[i].findAll('arxiv:affiliation') != []:
                                affiliationList.append([tag.string for tag in test[i].findAll('arxiv:affiliation')])

#for list in affiliationList:
#    list = list.strip(';')

G = nx.Graph()

for list in affiliationList:
    if len(list) > 10:
        print list
        for pos, node1 in enumerate(list):
            for node2 in list[pos:]:
                G.add_edge(node1, node2)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=100, node_color='blue')
nx.draw_networkx_edges(G, pos, edge_color='green')
nx.draw_networkx_labels(G, pos, font_color='red')

plt.axis('off')
plt.show()
