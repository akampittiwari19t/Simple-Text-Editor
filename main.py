#import tkinter for creating GUI apps

import tkinter as tk
from tkinter import filedialog,messagebox

# Main window code 
root = tk.Tk()
root.title(" Simple Text Editor ")
root.geometry("800x600")

#create text area 

Text=tk.Text(
    root,
    wrap=tk.WORD,
    font =("Helvetica",15)
)

Text.pack(expand=True,fill=tk.BOTH)

# Main LOgic starts now 

# function 1- to create a new file
 
def new_file():
    Text.delete(1.0,tk.END)

# Function 2 -to open a new file 
def open_file():
    # open file dialogue
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        #open the selected  file

        with open(file_path,"r") as file:
            Text.delete(1.0,tk.END)
            Text.insert(tk.END,file.read())  # data overwrite na ho iss liye tk.end liya hai

# Function 3 - save the file #LOcatio kaha save krna hai 

def save_file():
    #open save file dialogue 

    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    
    if file_path:
        with open(file_path,"w") as file:
            file.write(Text.get("1.0", tk.END))# Jo text hai vo sab file me save ho jae iss liye use kiya hai  

        messagebox.showinfo("info","File saved successfully")# iss liye use kiya ki show ho ji file save ho gai hai 

    #  Create Menu bar 

Menu=tk.Menu(root)
root.config(menu=Menu)
file_menu=tk.Menu(Menu)# root se connect hai se show kr diya 

    # New ,Open File ,Save,Exit

    # Add file menu to menu bar
Menu.add_cascade(label="File",menu=file_menu) # file ko add krna hai toh add cascade use krna hota hai
   
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

    




#starts and keeps the window open

root.mainloop()