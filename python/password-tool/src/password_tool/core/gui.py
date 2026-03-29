import tkinter as tk
from tkinter import ttk
from password_tool.core.checker import *
from password_tool.config import *



def toggle_password():
    if entry.cget("show") == "":
        entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        entry.config(show="")
        toggle_btn.config(text="Hide")

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("600x400")
root.resizable(False, False)

style = ttk.Style()
style.configure("Small.TButton", padding=(2, 1))
style.configure("Big.TButton", padding=(10, 8))
style.configure("Med.TButton", padding=(6, 4))


label = ttk.Label(root, text="Password Strength Checker")
label.place(relx=0.5, rely=0.05, anchor="center")

entry = ttk.Entry(root, width=30, show="*")
entry.place(relx=0.5, rely=0.15, anchor="center")


toggle_btn = ttk.Button(root, text="Show", style="Small.TButton", command=toggle_password)
toggle_btn.place(relx=0.72, rely=0.15, anchor="center")



button = ttk.Button(root, text="Submit", command=check_pass)
button.place(relx=0.5, rely=0.3, anchor="center")

output_label = ttk.Label(root, text="here?")
output_label.pack(pady=550)


root.mainloop()

