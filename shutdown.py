# Remeber to save your work befor running this script 
# importing necessary  module  you can do  "pip install tkinter" in terminal to install tkinter 
from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import *
import os
  
# Create the main window
root = Tk()

# Set the title of the window
root.title('Shut Down Windows')

# Function to be called when the button is clicked
def clicked():
    # Get the selected value from the combobox
    selected_val = combo.get()

    # Check the selected value and execute the corresponding command
    if selected_val=='Shutdown':
        os.system("shutdown /s /t 1")  # Shutdown command
    elif selected_val =='Restart':
        os.system("shutdown /r /t 1")  # Restart command

# Create a label to prompt the user for their choice
label = Label(root, text="What Do You Want Your Computer To Do : ")
label.grid(row=0, column=1)

# Create a button to trigger the clicked() function
button1 = Button(root, text='OK', command=clicked, style='TButton')
root.geometry('350x275')  # Set the initial size of the window
button1.grid(row=2, column=1)

# Configure layout for button adjustment 
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Create a combobox to allow the user to select between 'Shutdown' and 'Restart'
combo = Combobox(root)
combo['value'] = ['Shutdown','Restart']
combo.grid(row=1, column=1)

# Start the main event loop
root.mainloop()
