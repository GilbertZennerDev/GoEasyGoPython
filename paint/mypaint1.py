import os
import tempfile
import tkinter as tk

def rgb_to_tk(rgb):
    """Converts an RGB tuple to a Tkinter-compatible color string."""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

root = tk.Tk()
root.title('My Texture Generator')
root.geometry("800x650")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Convert RGB tuple to Tkinter-compatible color string
bgColor = rgb_to_tk((176, 68, 35))  # Red color in RGB format

# Draw a rectangle with the background color
canvas.create_rectangle(0, 0, 800, 600, fill=bgColor)

btnQuit = tk.Button(root, text="Quit", command=root.quit)
btnQuit.pack()

root.mainloop()
