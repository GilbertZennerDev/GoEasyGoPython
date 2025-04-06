import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("800x600")

result = "0"
resultValue = 0

values = []

def setResultField(value):
    resultField.delete("0", "end")
    resultField.insert(0, string=value)

def changeResult(value):
    result = resultField.get()
    if result == "0":
        result = value
    else:
        result += value
    setResultField(result)
    
def equal():
    result = resultField.get()
    print(f"[debug] equal {result}")
    if '+' in result:
        nbrs = result.split('+')
        resultValue = float(nbrs[0]) + float(nbrs[1])
        setResultField(resultValue)
    elif '-' in result:
        nbrs = result.split('-')
        resultValue = float(nbrs[0]) - float(nbrs[1])
        setResultField(resultValue)
    elif '*' in result:
        nbrs = result.split('*')
        resultValue = float(nbrs[0]) * float(nbrs[1])
        setResultField(resultValue)
    else:
        nbrs = result.split('/')
        resultValue = float(nbrs[0]) / float(nbrs[1])
        setResultField(resultValue)
        
def clear():
    setResultField("0")

resultField = tk.Entry(root, width=30)
resultField.insert(0, string=result)
resultField.grid(row=0, column=0)

_1Btn = tk.Button(root, text="1", command=lambda:changeResult("1"), width = 3)
_1Btn.grid(row=1, column=0)

_2Btn = tk.Button(root, text="2", command=lambda:changeResult("2"), width = 3)
_2Btn.grid(row=1, column=1)

_3Btn = tk.Button(root, text="3", command=lambda:changeResult("3"), width = 3)
_3Btn.grid(row=1, column=2)

_4Btn = tk.Button(root, text="4", command=lambda:changeResult("4"), width = 3)
_4Btn.grid(row=2, column=0)

_5Btn = tk.Button(root, text="5", command=lambda:changeResult("5"), width = 3)
_5Btn.grid(row=2, column=1)

_6Btn = tk.Button(root, text="6", command=lambda:changeResult("6"), width = 3)
_6Btn.grid(row=2, column=2)

_7Btn = tk.Button(root, text="7", command=lambda:changeResult("7"), width = 3)
_7Btn.grid(row=3, column=0)

_8Btn = tk.Button(root, text="8", command=lambda:changeResult("8"), width = 3)
_8Btn.grid(row=3, column=1)

_9Btn = tk.Button(root, text="9", command=lambda:changeResult("9"), width = 3)
_9Btn.grid(row=3, column=2)

_addBtn = tk.Button(root, text='+', command=lambda:changeResult("+"), width = 3)
_addBtn.grid(row=4, column=0)

_subBtn = tk.Button(root, text='-', command=lambda:changeResult("-"), width = 3)
_subBtn.grid(row=4, column=1)

_multBtn = tk.Button(root, text='*', command=lambda:changeResult("*"), width = 3)
_multBtn.grid(row=4, column=2)

_divBtn = tk.Button(root, text='/', command=lambda:changeResult("/"), width = 3)
_divBtn.grid(row=4, column=3)

_equalBtn = tk.Button(root, text='=', command=lambda:equal(), width = 3)
_equalBtn.grid(row=5, column=2)

_clearBtn = tk.Button(root, text='CE', command=lambda:setResultField("0"), width = 3)
_clearBtn.grid(row=6, column=2)

root.mainloop()