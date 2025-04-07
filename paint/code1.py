import random as rn
import time
from PIL import Image, ImageDraw
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def idle_5sec(event=None):
    """freeze the action for 5 seconds and save to file"""
    root.title("Idle for 5 seconds, save to file circles.png")
    time.sleep(5)
    root.title("Happy Circles ...")
    # PIL images can be saved as .png .jpg .gif or .bmp files
    filename = "happy_circles.jpg"
    # save the PIL image
    img_pil.save(filename)

# create the window form
root = tk.Tk()
# window title text
root.title("Happy Circles (click on window to idle for 5 seconds)")

# set width and height
w = 640
h = 480
# create the Tkinter canvas for drawing
cv_tk = tk.Canvas(width=w, height=h, bg='black')
cv_tk.pack()
# create a PIL canvas in memory and use in parallel
black = (0, 0, 0)
img_pil = Image.new("RGB", (w, h), black)
cv_pil = ImageDraw.Draw(img_pil)

# endless loop to draw the random circles
while True:
    # random center (x,y) and radius r
    x = rn.randint(0, w)
    y = rn.randint(0, h)
    r = rn.randint(5, 50)
    # create a random color for PIL and Tkinter
    # go from pil color (r, g, b) to tk color format "#rrggbb"
    color_pil = (rn.randrange(256), rn.randrange(256), rn.randrange(256))
    color_tk = '#' + "".join("%02x" % c for c in color_pil)
    # now draw the tk circle
    cv_tk.create_oval(x, y, x+r, y+r, fill=color_tk)
    # and the pil circle (memory only)
    cv_pil.ellipse((x, y, x+r, y+r), fill=color_pil, outline=black)
    # update the window
    root.update()
    # bind left mouse double click, idle for 5 seconds
    cv_tk.bind('<Double-1>', idle_5sec)

# start the program's event loop
root.mainloop()
