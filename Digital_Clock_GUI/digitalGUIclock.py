import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

#what is label in tkinter - A label in tkinter is a widget used to display text or images in a window.

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string) # Update the label with the current time
    label.after(1000, time) # Call the time function after 1000 milliseconds (1 second)

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white') # Create a label widget
label.pack(anchor='center') # Pack the label into the window
time() # Call the time function to start the clock
root.mainloop() # Start the Tkinter event loop