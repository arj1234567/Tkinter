from tkinter import *
from tkinter import Menu
window=Tk()
window.title('welcome to python')
window.geometry('400x200')
menu=Menu(window)
new_item=Menu(menu)
#new_item1=Menu(menu)
new_item.add_command(label='edit')
new_item.add_separator()
new_item.add_command(label='zoom')
menu.add_command(label="file")
menu.add_cascade(label="New",menu=new_item)
##new_item1.add_command(label='profile')
##new_item1.add_command(label='contact')
##menu.add_cascade(label='home',menu=new_item1)

window.config(menu=menu)
window.mainloop()
