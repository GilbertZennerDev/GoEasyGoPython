import tkinter as tk

root = tk.Tk()
root.title("GUI-Nano")
root.geometry("800x600")

def loadText():
    givenfilename = filenameEntry.get()
    if givenfilename == "":
        givenfilename = "text.txt"
    writtenText.delete('1.0', 'end')
    try:
        with open(givenfilename, "r") as file:
            writtenText.insert('1.0', file.read())
    except FileNotFoundError:
        print("Error: File not Found")

def saveText():
    givenfilename = filenameEntry.get()
    if givenfilename == "":
        givenfilename = "text.txt"
    with open(givenfilename, "w") as file:
        file.write(writtenText.get("1.0", "end"))

writtenText = tk.Text(root, height = 20, width = 100)
writtenText.pack()
filenameEntry = tk.Entry(root)
filenameEntry.pack()
btnSave = tk.Button(root, text="Save", command=saveText)
btnSave.pack()
btnLoad = tk.Button(root, text="Load", command=loadText)
btnLoad.pack()

root.mainloop()