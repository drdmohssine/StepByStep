from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "test"))
session = driver.session()

def getlnodes(steptitle):
    lnodes = session.run("Match(Step{Title: $steptitle}) OPTIONAL MATCH (Step)-[*..1]->(m) RETURN DISTINCT *",steptitle = steptitle)
    valueslst =lnodes.values()
    return valueslst
allnodes = getlnodes('Title Web')

class node(object):
    """__init__() functions as the class constructor"""
    def __init__(self, id=None, title=None, picture=None, text=None):
        self.id = id
        self.title = title
        self.picture = picture
        self.text = text
        
nodelist = []
nodelist.append(node(allnodes[0][0].id,allnodes[0][0]['Title'],allnodes[0][0]['Picture'],allnodes[0][0]['Text']))

for item in allnodes:
    indx = allnodes.index(item)
    nodelist.append(node(allnodes[indx][1].id,allnodes[indx][1]['Title'],allnodes[indx][1]['Picture'],allnodes[indx][1]['Text']))

