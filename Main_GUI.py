import tkinter as tk
from subprocess import Popen, PIPE

def callKruskal():
    Popen(['python','kruskal_gui.py'])

def callHuffman():
    Popen(['python','./huffman_gui.py'])

def callselection():
    Popen(['python','activitySelection_gui.py'])

def callFractional():
    Popen(['python','fractionalKnapsack_gui.py'])

def callDijkstra():
    Popen(['python','dijkstra_gui.py'])

mainWindow = tk.Tk()
mainWindow.title("Greedy Algorithms")
mainWindow.geometry("360x240")

lbl_select = tk.Label(text="Select algorithm:\n",bd=5)
lbl_select.pack()

frm_options = tk.Frame(master=mainWindow)
frm_options.pack()

btn_kruskal = tk.Button(
    master=frm_options, 
    text="Minimum Spanning Tree (Kruskal's algorithm)",
    width=50, 
    command=callKruskal,
    bd=3
)
btn_kruskal.pack()

btn_prim = tk.Button(
    master=frm_options, 
    text="Minimum Spanning Tree (Prim's Algorithm)",
    width=50,
    bd=3
)
# btn_prim.pack()

btn_huffman = tk.Button(
    master=frm_options, 
    text="Huffman Coding",
    width=50,
    command = callHuffman,
    bd=3
)
btn_huffman.pack()

btn_selection = tk.Button(
    master=frm_options, 
    text="Activity Selection",
    width=50,
    command = callselection,
    bd=3
)
btn_selection.pack()

btn_fractionalKnapsack = tk.Button(
    master=frm_options, 
    text="Fractional Knapsack",
    width=50,
    command = callFractional,
    bd=3
)
btn_fractionalKnapsack.pack()

btn_dijkstra = tk.Button(
    master=frm_options, 
    text="Shortest Distances from Single Source (Dijkstra's Algorithm)",
    width=50,
    command = callDijkstra,
    bd=3
)
btn_dijkstra.pack()

lbl_author = tk.Label(
    mainWindow,
    text="\nGUI Written by Hritvik Kaushik"
        +"\nLibrary used: Tkinter (Python 3.8.2)",
    bd=3
)
lbl_author.pack(side="bottom")

mainWindow.mainloop()