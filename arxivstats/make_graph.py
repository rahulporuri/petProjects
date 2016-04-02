import json
from collections import defaultdict
from graphcanvas.api import GraphView, graph_from_dict

testDict = defaultdict(dict)
alist = ['University of Michigan','MIT','Imperial College London','Pennsylvania State University','Universita degli Studi Roma Tre','INAF-IASF Bologna','INAF Arcetri','Rikkyo University','Columbia University','University of Leicester','Harvard-Smithsonian CfA','NASA/MSFC','ISAS','University of Kyoto']

for what in alist:
    testDict[what] = []
    for a in alist:
        if a != what:
            testDict[what].append(a)

#GraphView(graph=graph_from_dict(json.load(open('arxiv_data.dat')))).configure_traits()
GraphView(graph=graph_from_dict(testDict)).configure_traits()
