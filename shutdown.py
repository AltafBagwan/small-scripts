from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import *
import os
  

root = Tk()

root.title('Shut Down Windows')


def clicked():
    selected_val = combo.get()

    if selected_val=='Shutdown':
        os.system("shutdown /s /t 1")
    elif selected_val =='Restart':
        os.system("shutdown /r /t 1")
    

lable = Label(root,text="What Do You Want Your Computer To Do : ")
lable.grid(row=0,column=1)

button1 = Button(root,text='OK',command=clicked,style='TButton')
root.geometry('350x275')

button1.grid(row=2,column=1)

root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(2,weight=1)

combo = Combobox(root)

combo['value'] = ['Shutdown','Restart']
combo.grid(row=1,column=1)



root.mainloop()