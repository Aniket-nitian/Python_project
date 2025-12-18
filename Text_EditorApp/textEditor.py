# Text Editor Application
import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END) # Clear the text area

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get(1.0, tk.END)
            file.write(content)
            messagebox.showinfo("Save File", "File saved successfully!")

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")
text = tk.Text(root, wrap='word', font=('Arial', 12))
text.pack(expand=1, fill='both')

menu = tk.Menu(root) # Create a menu bar, used to hold menu items
root.config(menu=menu) # Configure the root window to use the menu bar
file_menu = tk.Menu(menu, tearoff=0) # Create a File menu, tearoff=0 means the menu cannot be separated from the window
menu.add_cascade(label="File", menu=file_menu) # Add the File menu to the menu bar
file_menu.add_command(label="New", command=new_file) # Add New command to the File menu
file_menu.add_command(label="Open", command=open_file) # Add Open command to the File menu
file_menu.add_command(label="Save", command=save_file)  # Add Save command to the File menu
file_menu.add_separator() # Add a separator line in the File menu
file_menu.add_command(label="Exit", command=root.quit) # Add Exit command to the File menu

text = tk.Text(root, wrap=tk.WORD, font=('Arial', 12)) # Create a text area widget with word wrapping and specified font
text.pack(expand=tk.YES, fill=tk.BOTH) # Pack the text area to expand and fill the window
root.mainloop() # Start the Tkinter event loop