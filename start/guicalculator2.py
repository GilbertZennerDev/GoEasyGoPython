import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("800x600")

result = ""

def changeResult(value):
    global result
    result += value
    resultField.delete("0", "end")
    resultField.insert(0, string=result)

def number_button(n):
    def press():
        changeResult(str(n))
    
    return press

# Create a frame to hold the number buttons
number_buttons_frame = tk.Frame(root)
number_buttons_frame.grid(row=1, column=0, columnspan=3) 

for i in range(1, 10):
    btn = tk.Button(number_buttons_frame, text=str(i), command=number_button(i))
    btn.grid(row=0, column=i-1)

resultField = tk.Entry(root, width=30)
resultField.insert(0, string=result)
resultField.grid(row=0, column=0)

# Zero button
zeroBtn = tk.Button(root, text="0", command=lambda: changeResult("0"))
zeroBtn.grid(row=1, column=1)

# Decimal point button
dotBtn = tk.Button(root, text=". ", command=lambda: changeResult("."))
dotBtn.grid(row=1, column=2)

# Operation buttons (Add, Subtract, Multiply, Divide)
addBtn = tk.Button(root, text="+", command=lambda: changeResult(" + "))
addBtn.grid(row=4, column=0)

subBtn = tk.Button(root, text="-", command=lambda: changeResult("-"))
subBtn.grid(row=4, column=1)

mulBtn = tk.Button(root, text="*", command=lambda: changeResult("*"))
mulBtn.grid(row=4, column=2)

divBtn = tk.Button(root, text="/", command=lambda: changeResult("/"))
divBtn.grid(row=5, column=0)

# Equal button
equalBtn = tk.Button(root, text="=", command=lambda: eval(resultField.get()))
equalBtn.grid(row=4, column=3)

root.mainloop()
