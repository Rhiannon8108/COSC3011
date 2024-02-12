import tkinter as tk 

root = tk.Tk()
root.title("Desktop Application")
root.geometry("750x500")

label = tk.Label(root, width=22, text="Hello World", anchor = 'w')
label.config(font=("Raleway", 16))
label.pack(side=tk.TOP, pady = 30)

row = tk.Frame(root)
label = tk.Label(row, width=22, text="Hello World", anchor='w')
lable.config(font=("Raleway", 16))

root.mainloop() 
