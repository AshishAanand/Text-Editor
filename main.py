import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

# Functions for File Operations
def new_file():
    text_area.delete(1.0, tk.END)
    status_bar.config(text="New File")

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        status_bar.config(text=f"Opened: {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        status_bar.config(text=f"Saved: {filepath}")

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def undo_action():
    try:
        text_area.edit_undo()
    except tk.TclError:
        messagebox.showinfo("Undo", "Nothing to undo.")

def redo_action():
    try:
        text_area.edit_redo()
    except tk.TclError:
        messagebox.showinfo("Redo", "Nothing to redo.")

def about_app():
    messagebox.showinfo("About", "This is a basic text editor built with Tkinter.")

# Create the Main Window
root = tk.Tk()
root.title("My Text Editor")
root.geometry("800x600")

# Create the Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo_action)
edit_menu.add_command(label="Redo", command=redo_action)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_app)

# Create the Toolbar
toolbar = ttk.Frame(root, padding=2)
toolbar.pack(side=tk.TOP, fill=tk.X)

open_btn = ttk.Button(toolbar, text="Open", command=open_file)
open_btn.pack(side=tk.LEFT, padx=2, pady=2)

save_btn = ttk.Button(toolbar, text="Save", command=save_file)
save_btn.pack(side=tk.LEFT, padx=2, pady=2)

cut_btn = ttk.Button(toolbar, text="Cut", command=cut_text)
cut_btn.pack(side=tk.LEFT, padx=2, pady=2)

copy_btn = ttk.Button(toolbar, text="Copy", command=copy_text)
copy_btn.pack(side=tk.LEFT, padx=2, pady=2)

paste_btn = ttk.Button(toolbar, text="Paste", command=paste_text)
paste_btn.pack(side=tk.LEFT, padx=2, pady=2)

# Add Undo and Redo Buttons to the Toolbar
undo_btn = ttk.Button(toolbar, text="Undo", command=undo_action)
undo_btn.pack(side=tk.LEFT, padx=2, pady=2)

redo_btn = ttk.Button(toolbar, text="Redo", command=redo_action)
redo_btn.pack(side=tk.LEFT, padx=2, pady=2)

# Create the Text Editing Area
text_area = tk.Text(root, wrap="word", undo=True, font=("Arial", 15))
text_area.pack(expand=True, fill="both", padx=5, pady=5)

# Create the Status Bar
status_bar = ttk.Label(root, text="Welcome to My Text Editor", anchor="w")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Start the Main Loop
root.mainloop()
