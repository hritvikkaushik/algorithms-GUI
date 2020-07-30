import dijkstra
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Dijkstra's Algorithm")

frames = []
fields = []
labels = []

source = None

def getSourceNode():
    global source
    source=ent_sourceNode.get()
    frm_sourceNode.pack_forget()
    btn_addEdge.pack_forget()
    lbl = tk.Label(mainWindow,text="Source Node: " + str(source))
    lbl.pack()
    btn_addEdge.pack()
    btn_getEdgeValues.pack()

def createEdgeValues():
    global fields
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
        fields.append(widget)

        widget.pack(side="left")

def getEdgeValues():
    btn_addEdge.pack_forget()
    edgeFrom = None
    edgeTo = None
    edgeCost = None
    nodes = []
    distances = {}
    for edge in range(len(fields)):
        if (edge%3 == 0):
            frames[edge//3].pack_forget()
            edgeFrom = fields[edge].get()
            if edgeFrom not in nodes:
                nodes += edgeFrom
                distances[edgeFrom] = {}
        elif (edge%3 == 1):
            edgeTo = fields[edge].get()
            if edgeTo not in nodes:
                nodes += edgeTo
                distances[edgeTo] = {}
        else:
            edgeCost = fields[edge].get()
            edgeCost = int(edgeCost)
            distances[edgeFrom][edgeTo] = edgeCost
            distances[edgeTo][edgeFrom] = edgeCost
            label = tk.Label(mainWindow,text="Edge " + str(int((edge+1)/3)) + " from " + str(edgeFrom) + " to " + str(edgeTo) + ", cost: " + str(edgeCost))
            label.pack()
    btn_getEdgeValues.pack_forget()
    lbl_minimumDistances = tk.Label(
        mainWindow,
        text="The minimum distance to each node from \'"
            +str(source)
            +"\' is: \n"
    )
    lbl_minimumDistances.pack()
    minimumDistances = dijkstra.getDistances(nodes,distances,source)
    print(minimumDistances)
    for node,distance in minimumDistances.items():
        lbl=tk.Label(mainWindow,text=str(node)+": "+str(distance))
        lbl.pack()
        
lbl_intro=tk.Label(mainWindow, 
    bd=5, 
    text= "This is an interface to get the Shortest Path to all nodes from a single source, using Dijkstra's Algorithm."
        +"\nComplexity = O(|E| + |V|log|V|)"
        +"\nFirst, enter the name of the source vertex in the given field."
        +"\nThen, use the 'Add Edge' button to add as many edges as needed."
        +"\nFill all the edge details. There must be only one edge between any two nodes."
        +"\nPress the 'Finalise Edge Values' button to insert all the values."
        +"\nFinally, press the 'Get Distances' button to get the minimum distances."
)
lbl_intro.pack()


frm_sourceNode = tk.Frame(master=mainWindow, width=60, borderwidth=3)
lbl_sourceNode = tk.Label(master=frm_sourceNode, text="Enter source node: ")
lbl_sourceNode.pack(side=tk.LEFT)
ent_sourceNode = tk.Entry(master=frm_sourceNode, width=8)
ent_sourceNode.pack(side=tk.LEFT)
btn_sourceNode = tk.Button(master=frm_sourceNode, text="Enter", command= getSourceNode)
btn_sourceNode.pack(side=tk.LEFT)
frm_sourceNode.pack()

frm_finalButtons = tk.Frame(mainWindow,borderwidth=3)
frm_finalButtons.pack(side="bottom")

btn_addEdge = tk.Button(mainWindow, text="Add Edge", command=createEdgeValues)

btn_getEdgeValues = tk.Button(frm_finalButtons, text="Insert All Edge Values", command=getEdgeValues)

mainWindow.mainloop()