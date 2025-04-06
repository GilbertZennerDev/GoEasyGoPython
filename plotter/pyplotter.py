import os
os.environ['MPLBACKEND'] = 'TkAgg'

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Replace 'TkAgg' with 'Qt5Agg' if you prefer


# importing matplotlib
import matplotlib.pyplot as plt 
 
 
# making a simple plot
x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]
 
# creating error
y_error = 0.2
 
# plotting graph
plt.plot(x, y)
 
plt.errorbar(x, y,
             yerr = y_error,
             fmt ='o')