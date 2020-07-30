import tkinter as tk
import fractionalKnapsack

mainWindow = tk.Tk()
mainWindow.title("Fractional Knapsack")

lbl_intro=tk.Label(mainWindow, 
    bd=5, 
    text= "This is an interface to select the maximum value possible\nwhen a fraction of an item can be selected."
    +"\nComplexity: O(n)+O(n log n) = O(n log n)"
    +"\nFirst, enter the capacity of the backpack."
    +"\nNext, create as many items as needed using the button."
    +"\nEnter the corresponding weights and values of the items."
    +"\nFinally, click the Select Maximum Value button to select the maximum value."
)
lbl_intro.pack()

weights = []
values = []

frames = []
labels = []
widgets = []
capacity=0

lbl_gotCapacity = tk.Label()
lbl_maxValue = tk.Label()


def getCapacity():
    global capacity
    capacity = int(ent_getCapacity.get())
    global lbl_gotCapacity
    ent_getCapacity.pack_forget()
    btn_getCapacity.pack_forget()
    lbl_getCapacity.pack_forget()
    lbl_gotCapacity.pack_forget()
    btn_addItem.pack_forget()
    lbl_gotCapacity = tk.Label(mainWindow,text="Capacity of backpack: " + str(capacity) )
    lbl_gotCapacity.pack()
    btn_addItem.pack()

def createItem():

    global labels
    global frames
    global widgets

    frame = tk.Frame(mainWindow, borderwidth=2)
    frames.append(frame)

    frame.pack(side="top")

    label=tk.Label(frame,text="Item " + str(len(frames)) + ":   Weight: ")
    labels.append(label)
    label.pack(side="left")
    widget1 = tk.Entry(frame,width=5,borderwidth=3)
    widget1.pack(side="left")
    label=tk.Label(frame,text=" Cost: ")
    labels.append(label)
    label.pack(side="left")
    widget2 = tk.Entry(frame,width=5,borderwidth=3)
    widget2.pack(side="left")

    widgets.append([widget1,widget2])

def getItems():
    count=0
    btn_getItems.pack_forget()
    btn_addItem.pack_forget()
    for (wt,val) in widgets:
        weights.append(int(wt.get()))
        values.append(int(val.get()))
        label = tk.Label(
            mainWindow,
            text="Item " + str(count) 
                + ", weight: " + str(weights[count]) 
                + ", cost: " + str(values[count]) 
        )
        label.pack()
        count += 1
    
    for frame in frames:
        frame.pack_forget()

    selectItems()

def selectItems():
    global lbl_maxValue
    lbl_maxValue.pack_forget()
    maxValue = fractionalKnapsack.getMaxValue(weights,values,capacity)
    lbl_maxValue = tk.Label(mainWindow,text="Maximum value selected from backpack is: "+str(maxValue))
    lbl_maxValue.pack()

frm_getCapacity = tk.Frame(mainWindow)
frm_getCapacity.pack()
lbl_getCapacity = tk.Label(frm_getCapacity, text="Enter Capacity of backpack: ", bd=5)
lbl_getCapacity.pack(side="left")
ent_getCapacity = tk.Entry(frm_getCapacity)
ent_getCapacity.pack(side="left")
btn_getCapacity = tk.Button(frm_getCapacity, text="Enter", command=getCapacity)
btn_getCapacity.pack(side="left")

btn_addItem = tk.Button(mainWindow, text="Create Item", command=createItem, bd=3)
btn_addItem.pack()
frm_finalButtons = tk.Frame(mainWindow)
frm_finalButtons.pack(side="bottom")
btn_getItems = tk.Button(frm_finalButtons, text="Finalise Items", command=getItems)
btn_getItems.pack(side="left")

mainWindow.mainloop()