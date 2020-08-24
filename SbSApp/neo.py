from neo4j import GraphDatabase

#On Browser http://localhost:7474/browser/
driver = GraphDatabase.driver("bolt://172.17.0.3:7687", auth=("neo4j", "test"))
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "test"))
session = driver.session()


def add_friend(tx, name, friend_name):
    tx.run("MERGE (a:Person {name: $name}) "
           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)

def print_friends(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
        print(record["friend.name"])

with driver.session() as session:
    session.write_transaction(add_friend, "Arthur", "Guinevere")
    session.write_transaction(add_friend, "Arthur", "Lancelot")
    session.write_transaction(add_friend, "Arthur", "Merlin")
    session.read_transaction(print_friends, "Arthur")


with driver.session() as session:
    session.read_transaction(print_friends, "Arthur")




def tstneo(name):
    result = session.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
    "RETURN friend.name ORDER BY friend.name", name=name)
    return result


name = "Arthur"
result = result = session.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
    "RETURN friend.name ORDER BY friend.name", name=name)

result = session.run("Match(Step{Title: 'Step 2'}) OPTIONAL MATCH (Step)-[*..1]->(m) RETURN DISTINCT *")

dir(result)
friends = result.value()
friends[0]
test = tstneo("Arthur")
entire_result = [] # Will contain all the items
for record in test:
    entire_result.append(record)

dir(entire_result[0])
entire_result[0].value()


textvalue='txtvalue'
picturevalue='pvalue'
titlevalue='tvalue'
session.run("CREATE (stp6:Step { Title: $title, Text: $text, Picture: $picture })",title=titlevalue, text=textvalue, picture=picturevalue)

session.run("MATCH (s5:Step) WHERE s5.Title = 'Step 5' "
"MATCH (s6:Step) WHERE s6.Title = 'title from django'"
"CREATE (s5)-[r:CONTAIN]->(s6)")




stepid = 105
getnode = session.run("MATCH (s) WHERE ID(s) = $stepid RETURN  s",stepid=stepid)
valueslst =getnode.values()
id = valueslst[0].id
labels = valueslst[0].labels
Title = valueslst[0]['Title']
Picture = valueslst[0]['Picture']
Text = valueslst[0]['Text']

tst = my_function(127)
tst.id

def getnodefunc(stepid):
    node = session.run("MATCH (s) WHERE ID(s) = $stepid RETURN  s",stepid=stepid)
    valueslst =node.values()
    return valueslst[0]
getnode = getnodefunc(104)

type(getnode)

class getnodeclass():
    def __init__(self,sid):
        self.sid = sid
        getnode = getnodefunc(self.sid)
        id = getnode.id
        labels = getnode.labels
        title = getnode['Title']
        picture = getnode['Picture']
        text = getnode['Text']
        self.id = id
        self.labels = labels
        self.title = title
        self.picture = picture
        self.text = text
        print(getnode)

    
    

    """
    getnode = getnodefunc2()
    id = getnode.id
    labels = getnode.labels
    title = getnode['Title']https://pbs.twimg.com/media/EUnIZTOU4AEqQZP?format=jpg&name=large
    picture = getnode['Picture']
    text = getnode['Text']
    """

nodeobj = getnodeclass(sid=104)
dir(nodeobj)
nodeobj.picture

def getlnodes(nid):
    lnodes = session.run("MATCH (s) WHERE ID(s) = $nid OPTIONAL MATCH (s)-[*..1]->(m) RETURN * ORDER BY m.idx",nid = nid)
    valueslst =lnodes.values()
    return valueslst

allnodes[0][0].id
allnodes[0][0]['Title']
allnodes[0][0]['Picture']
allnodes[0][0]['Text']


class node(object):
    """__init__() functions as the class constructor"""
    def __init__(self, id=None, title=None, picture=None, text=None,subnodes=None):
        self.id = id
        self.title = title
        self.picture = picture
        self.text = text
        self.subnodes = subnodes

def testsubnod(nid):
    thrdtest = getlnodes(nid)
    if thrdtest[0][0] is None:
        return False
    else:
        return True


allnodes = getlnodes(105) 

node0list = []
node0list.append(node(allnodes[0][1].id,allnodes[0][1]['Title'],allnodes[0][1]['Picture'],allnodes[0][1]['Text'],subnodes=(testsubnod(allnodes[0][1].id))))
node1list = []
for item in allnodes:
    indx = allnodes.index(item)
    node1list.append(node(allnodes[indx][0].id,allnodes[indx][0]['Title'],allnodes[indx][0]['Picture'],allnodes[indx][0]['Text'],subnodes=(testsubnod(allnodes[indx][0].id))))

node1list[5].subnodes

testsubnod(105)

node1list[0].id
node1list[1].id


allnodes = getlnodes(nid=104)
allnodes[0][0].id
allnodes[0][1].id

allnodes[0][0]
allnodes[1][0]
allnodes[2][0]

def getallsteps():
    allsteps = session.run("MATCH (n:Step) RETURN (n)")
    return allsteps.value()
AllSteps = getallsteps()
AllSteps[0]['Title']
for itm in AllSteps:
    print("the id is:"+str(itm.id)+ " the title is: "+str(itm['Title']))


crstp=session.run("CREATE (s:Step { Title: 'tt2', Text: 'dsfdkljfs', Picture: 'sdofjpsjdof' }) RETURN (s)" )
vcrstp = crstp.value()[0].id
vcrstp[0].id

session.run("MATCH (s0) WHERE ID(s0)  = 104 "
"MATCH (s1) WHERE ID(s1)= $childid "
" CREATE (s0)-[r:CONTAIN { idx:$rindex}]->(s1) RETURN r",childid=vcrstp[0].id,rindex=len(node1list))

MATCH (s0) WHERE ID(s0)  = int(id)
MATCH (s1) WHERE ID(s1)= 128
CREATE (s0)-[r:CONTAIN { idx:3}]->(s1)
RETURN r

def getparentnodes(nid):
    pnodes = session.run("MATCH (s0:Step)<-[:CONTAIN]-(s1:Step) WHERE id(s0) = $nid RETURN id(s1),s1.Title",nid = nid)
    parentsval =pnodes.values()
    return parentsval

getparents = getparentnodes(148)
len(getparents)
getparents[1][1]