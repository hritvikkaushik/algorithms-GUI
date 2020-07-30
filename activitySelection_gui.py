import tkinter as tk
import activitySelection

mainWindow = tk.Tk()
mainWindow.title("Activity Selection")

startTimes=[]
finishTimes=[]

frames = []
labels = []
widgets = []

lbl_intro=tk.Label(mainWindow, 
    bd=5, 
    text= "This is an interface for the greedy algorithm for activity selection"
        +"\nKindly enter the activities, sorted by finish time"
        +"\nComplexity = O(N)"
        +"\nThen, use the 'Add Activity' button to add as many activities as needed."
        +"\nFill all the start and finish times."
        +"\nThen press the 'Finalise activities' button."
        +"\nFinally, press the 'Select Maximum Activities' button to get the selected activities."
)
lbl_intro.pack()

def createActivity():

    global labels
    global frames
    global widgets

    frame = tk.Frame(mainWindow, borderwidth=2)
    frames.append(frame)

    frame.pack(side="top")

    label=tk.Label(frame,text="Activity " + str(len(frames)) + ":   Starting time: ")
    labels.append(label)
    label.pack(side="left")
    widget1 = tk.Entry(frame,width=5,borderwidth=3)
    widget1.pack(side="left")
    label=tk.Label(frame,text=" Finishing time: ")
    labels.append(label)
    label.pack(side="left")
    widget2 = tk.Entry(frame,width=5,borderwidth=3)
    widget2.pack(side="left")

    widgets.append([widget1,widget2])


def getActivities():
    count=0
    btn_addActivity.pack_forget()

    for (start,finish) in widgets:
        startTimes.append(int(start.get()))
        finishTimes.append(int(finish.get()))
        label = tk.Label(
            mainWindow,
            text="Activity " + str(count) 
                + " from " + str(startTimes[count]) 
                + " to " + str(finishTimes[count]) 
        )
        label.pack()
        count += 1
    
    for frame in frames:
        frame.pack_forget()
    btn_getActivities.pack_forget()
    selectActivities()


def selectActivities():
    activitySelection.ActivitySelection(startTimes,finishTimes,len(startTimes))
    label_finished = tk.Label(mainWindow, text="Selected activites are: ", bd=3)
    label_finished.pack()
    for x in activitySelection.selected:
        label = tk.Label(
            mainWindow,
            text="Activity " + str(x) 
                + " from " + str(startTimes[x]) 
                + " to " + str(finishTimes[x]) 
        )
        label.pack()


btn_addActivity = tk.Button(mainWindow, text="Create Activity", command=createActivity, bd=3)
btn_addActivity.pack()


frm_finalButtons = tk.Frame(mainWindow)
frm_finalButtons.pack(side="bottom")
btn_getActivities = tk.Button(frm_finalButtons, text="Finalise Activities", command=getActivities)
btn_getActivities.pack(side="left")

mainWindow.mainloop()