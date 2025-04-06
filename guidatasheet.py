import tkinter as tk
import random

root = tk.Tk()
root.title("GUI-Nano")
root.geometry("800x600")
root.attributes('-fullscreen', True)

def loadText():
    content = []
    givenfilename = "text.txt"
    #givenfilename = filenameEntry.get()
    #if givenfilename == "":
    #    givenfilename = "text.txt"
    try:
        with open(givenfilename, "r") as file:
            all_lines = file.read().splitlines()
            for i, content in enumerate(all_lines):
                cells[i].delete('1.0', 'end')
                cells[i].insert('1.0', content)
    except FileNotFoundError:
        print("Error: File not Found")

def saveText():
    #givenfilename = filenameEntry.get()
    #if givenfilename == "":
    #    givenfilename = "text.txt"
    givenfilename = "text.txt"
    with open(givenfilename, "w+") as file:
        for i, content in enumerate(cells):
            file.write(content.get("1.0", "end"))
            
def genRandomData():
    for i, content in enumerate(cells):
        cells[i].delete('1.0', 'end')
        cells[i].insert('1.0', random.random())
        
def clearData():
    for i, content in enumerate(cells):
        cells[i].delete('1.0', 'end')
        cells[i].insert('1.0', "")

def quit():
    root.quit()

cells = []
# Create a grid layout
for j in range(20):
    for i in range(20):  # Number of cells
        cell = tk.Text(root, height=1, width=10)
        cell.grid(row=i+1, column=j)
        cells.append(cell)

btnRandomData = tk.Button(root, text="Random", command=genRandomData)
btnRandomData.grid(row = 0, column = 0)

btnClearData = tk.Button(root, text="Clear", command=clearData)
btnClearData.grid(row = 0, column = 1)

btnSave = tk.Button(root, text="Save", command=saveText)
btnSave.grid(row = 0, column = 2)

btnLoad = tk.Button(root, text="Load", command=loadText)
btnLoad.grid(row = 0, column = 3)

btnQuit = tk.Button(root, text="Quit", command=quit)
btnQuit.grid(row = 0, column = 4)
#btnLoad.pack()

root.mainloop()