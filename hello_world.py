import tkinter as tk 

root = tk.tk()
root.title("Desktop Application")
root.geometry("750x500")

lable = tk.Label(root, width=22, text="Hello World", anchor = 'w')
lable.config(font=("Raleway", 16))
lable.pack(side=tk.TOP, pady = 30)

row = tk.Frame(root)
label = tk.Label(row, width=22, text="Hello World", anchor='w')
lable.config(font=("Raleway", 16))

