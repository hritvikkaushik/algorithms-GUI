import tkinter as tk
import huffman

mainWindow = tk.Tk()
mainWindow.title("Huffman Coding")

lbl_intro=tk.Label(mainWindow, 
    bd=5, 
    text= "This is an interface to get the Huffman coding for entered string."
    + "\nComplexity = O(n log n), where n is the number of characters."
)
lbl_intro.pack()

inputString=""

lbl_showEncoding = tk.Label(
        mainWindow,
        text = "Symbol\tFrequency\tHuffman Code",
        bd=5
    )
lbl_encodedSymbols = []
lbl_showEncodedString = tk.Label(mainWindow)

def getString():
    global lbl_showEncodedString
    lbl_showEncodedString.pack_forget()
    for x in reversed(lbl_encodedSymbols):
        x.pack_forget()
        lbl_encodedSymbols.pop()
    
    lbl_showEncoding.pack_forget()
    inputString = ent_getString.get()
    huffman.data = inputString
    huffman.getEncoding()    
    lbl_showEncoding.pack()

    for p in huffman.huff:
        lbl_encodedSymbol = tk.Label(
            mainWindow,
            text = p[0] +'\t\t'+  str(huffman.frequency[p[0]]) + '\t\t' + p[1]
        )
        lbl_encodedSymbols.append(lbl_encodedSymbol)
        lbl_encodedSymbol.pack()

    lbl_showEncodedString = tk.Label(
        mainWindow,
        text = "The encoded string is:\n" + huffman.encodedString,
        bd = 5
    )
    lbl_showEncodedString.pack()

frm_getString = tk.Frame(mainWindow)
frm_getString.pack()
lbl_getString = tk.Label(frm_getString, text="Enter string to be encoded: ", bd=5)
lbl_getString.pack(side="left")
ent_getString = tk.Entry(frm_getString)
ent_getString.pack(side="left")
btn_getString = tk.Button(frm_getString, text="Enter", command=getString)
btn_getString.pack(side="left")

mainWindow.mainloop()