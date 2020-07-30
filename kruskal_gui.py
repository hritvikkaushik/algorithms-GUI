import tkinter as tk
import kruskal

mainWindow = tk.Tk()
mainWindow.title("Kruskal's Minimum Spanning Tree")

nVertices=0
nEdges=0

frames = []
edgeValues = []
labels = []

graph = kruskal.Graph(nVertices)

def getVertices():
    nVertices=ent_nVertices.get()
    global graph
    graph=kruskal.Graph(int(nVertices))
    frm_nVertices.pack_forget()
    lbl_graphMade = tk.Label(mainWindow,text="Graph initialised with " + str(nVertices) + " vertices")
    lbl_graphMade.pack()
    btn_addEdge.pack(side="top")
    btn_getEdgeValues.pack(side="left")
    btn_buildTree.pack(side="bottom")

def createEdgeValues():
    global edgeValues
    global frames
    global labels

    frame = tk.Frame(mainWindow, borderwidth=2)
    frames.append(frame)

    frame.pack(side="top")

    for i in range(3):
        if(i==0):
            label=tk.Label(frame,text="Edge " + str(len(frames)) + ":   From: ")
            labels.append(label)
            label.pack(side="left")
        elif(i==1):
            label=tk.Label(frame,text=" To: ")
            labels.append(label)
            label.pack(side="left")
        else:
            label=tk.Label(frame,text=" Cost: ")
            labels.append(label)
            label.pack(side="left")
        widget = tk.Entry(frame,width=5,borderwidth=3)
        edgeValues.append(widget)

        widget.pack(side="left")

def getEdgeValues():
    edgeFrom=None
    edgeTo=None
    edgeCost=None
    btn_addEdge.pack_forget()
    btn_getEdgeValues.pack_forget()
    for edge in range(len(edgeValues)):
        if (edge%3 == 0):
            frames[edge//3].pack_forget()
            edgeFrom = edgeValues[edge].get()
            edgeFrom = int(edgeFrom)
        elif (edge%3 == 1):
            edgeTo = edgeValues[edge].get()
            edgeTo = int(edgeTo)
        else:
            edgeCost = edgeValues[edge].get()
            edgeCost = int(edgeCost)
            graph.addEdge(edgeFrom,edgeTo,edgeCost)
            label = tk.Label(mainWindow,text="Edge " + str(int((edge+1)/3)) + " from " + str(edgeFrom) + " to " + str(edgeTo) + ", cost: " + str(edgeCost))
            label.pack()
            
        

def buildtree():
    global graph
    graph.KruskalMST()
    btn_buildTree.pack_forget()
    lbl_treeBuilt = tk.Label(mainWindow, text="Tree built! Edges of MST are as follows:")
    lbl_treeBuilt.pack()
    for u,v,cost in graph.result:
        label = tk.Label(mainWindow,text="Edge from "+str(u)+" to "+str(v)+", cost: "+str(cost))
        label.pack()
        



lbl_intro=tk.Label(mainWindow, 
    bd=8, 
    text= "\nThis is an interface to get the MST for an entered graph, using Kruskal's algorithm."
        +"\nComplexity = O(Elog(V))."
        +"\nFirst, enter the number of vertices and select enter."
        +"\nThen, use the 'Add Edge' button to add as many edges as needed."
        +"\nFill all the edge details. Vertex number must be given to 'from' and 'to' fields,"
        +"\nVertex numbers start from 0."
        +"\nThen press the 'Finalise Edge Values' button."
        +"\nFinally, press the 'Build Tree' button to get the edges of the tree."
)
lbl_intro.pack()


frm_nVertices = tk.Frame(master=mainWindow, width=60, borderwidth=3)
lbl_nVertices = tk.Label(master=frm_nVertices, text="Enter number of vertices: ", width=25)
lbl_nVertices.pack(side=tk.LEFT)
ent_nVertices = tk.Entry(master=frm_nVertices, width=20)
ent_nVertices.pack(side=tk.LEFT)
btn_nVertices = tk.Button(master=frm_nVertices, text="Enter", command= getVertices)
btn_nVertices.pack(side=tk.LEFT)
frm_nVertices.pack()

frm_finalButtons = tk.Frame(mainWindow,borderwidth=3)
frm_finalButtons.pack(side="bottom")

btn_addEdge = tk.Button(mainWindow, text="Add Edge", command=createEdgeValues)

btn_getEdgeValues = tk.Button(frm_finalButtons, text="Finalise Edge Values", command=getEdgeValues)


btn_buildTree = tk.Button(frm_finalButtons, text="Build MST", command=buildtree)


mainWindow.mainloop()