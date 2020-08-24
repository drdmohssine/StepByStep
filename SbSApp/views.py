from django.shortcuts import render
from django.http import HttpResponse
from .forms import GetStepId

from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://172.17.0.4:7687", auth=("neo4j", "test"))
session = driver.session()
# Create your views here.



def getlnodes(nid):
    lnodes = session.run("MATCH (s) WHERE ID(s) = $nid OPTIONAL MATCH (s)-[*..1]->(m) RETURN * ORDER BY m.idx",nid = nid)
    valueslst =lnodes.values()
    return valueslst

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
     
def getallsteps():
    allsteps = session.run("MATCH (n:Step) RETURN (n)")
    return allsteps.value()


def home(request):
    
    textvalue=request.POST.get('text')
    picturevalue=request.POST.get('picture')
    titlevalue=request.POST.get('title')
    if titlevalue is not None: 
        createstep = session.run("CREATE (s:Step { Title: $title, Text: $text, Picture: $picture }) RETURN (s)",title=titlevalue, text=textvalue, picture=picturevalue)
    

    
    AllSteps = getallsteps()
    allstepslist = []
    for item in AllSteps:
        allstepslist.append(node(item.id,item['Title'],item['Picture'],item['Text']))


   
    return render(request, 'home.html', {'allstepslist':allstepslist})

def getnode(request, id):

    allnodes = getlnodes(nid=int(id))
    node0list = []
    node0list.append(node(allnodes[0][1].id,allnodes[0][1]['Title'],allnodes[0][1]['Picture'],allnodes[0][1]['Text'],subnodes=(testsubnod(allnodes[0][1].id))))
    node1list = []
    if allnodes[0][0] is not None:
        for item in allnodes:
            indx = allnodes.index(item)
            node1list.append(node(allnodes[indx][0].id,allnodes[indx][0]['Title'],allnodes[indx][0]['Picture'],allnodes[indx][0]['Text'],subnodes=(testsubnod(allnodes[indx][0].id))))

    AllSteps = getallsteps()
    allstepslist = []
    for item in AllSteps:
        allstepslist.append(node(item.id,item['Title'],item['Picture'],item['Text']))

    def getparentnodes(nid):
        pnodes = session.run("MATCH (s0:Step)<-[:CONTAIN]-(s1:Step) WHERE id(s0) = $nid RETURN id(s1),s1.Title",nid = nid)
        parentsval =pnodes.values()
        return parentsval
    getparents = getparentnodes(int(id))

    textvalue=request.POST.get('text')
    picturevalue=request.POST.get('picture')
    titlevalue=request.POST.get('title')

    updateidvalue=request.POST.get('updateid')
    updatetextvalue=request.POST.get('updatetext')
    updatepicturevalue=request.POST.get('updatepicture')
    updatetitlevalue=request.POST.get('updatetitle')

    if updateidvalue is not None: 
        session.run("MATCH (s) WHERE ID(s) = $nodeid "
        "SET s.Picture = $picture "
        "SET s.Text = $text "
        "SET s.Title = $title "
        "RETURN (s) ",nodeid=int(updateidvalue),title=updatetitlevalue, text=updatetextvalue, picture=updatepicturevalue)
        

    if titlevalue is not None: 
        createstep = session.run("CREATE (s:Step { Title: $title, Text: $text, Picture: $picture }) RETURN (s)",title=titlevalue, text=textvalue, picture=picturevalue)
        session.run("MATCH (s0) WHERE ID(s0)  = $parentid "
        "MATCH (s1) WHERE ID(s1)= $childid "
        " CREATE (s0)-[r:CONTAIN { idx:$rindex}]->(s1) RETURN r",parentid=int(id),childid=createstep.value()[0].id,rindex=len(node1list))


    return render(request, 'steps.html', {'node0list': node0list,'node1list':node1list,'getparents':getparents,})


def deletenode(request, id):
    if request.method == "POST":
        session.run("MATCH (p:Step) where ID(p) = $nodeid OPTIONAL MATCH (p)-[r]-() DELETE r,p", nodeid=int(id))
    return render(request, 'steps.html')
    
