# Importing Libraries 
import customtkinter as ctk 
  
#Modes: system (default), light, dark
ctk.set_appearance_mode("dark")

#Themes: blue (default), dark-blue, green
ctk.set_default_color_theme("green")  

#Create a window
root = ctk.CTk()
root.title("Desktop Application")
root.geometry("750x500")

# Create a button and set text 
button = ctk.CTkButton(master=root, text ="Hello World!")

# place button in the center of the window 
button.place(relx=0.5, rely=0.5, anchor="center") 

# run the app 
root.mainloop()
