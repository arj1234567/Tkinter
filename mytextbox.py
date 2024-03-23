##from tkinter import *
##window = Tk()
##window.title("welcome to tkinter")
##window.geometry('700x600')
##lbl = Label(window,text="hai")
##lbl.grid(column=0,row=0)
##txt = Entry(window,width=10)
##txt.grid(column=0,row=1)
##def click():
##    res = "hello from" +txt.get()
##    lbl.configure(text=res)
##
##btn = Button(window,text="click me",command = click,bg="red",fg="white")
##btn.grid(column = 1,row=1)
##from tkinter import *
##from tkinter.ttk import *
##window = Tk()
##window.title("welcome to tkinter")
##window.geometry('700x600')
##lbl = Label(window,text="hai")
##lbl.grid(column=0,row=0)
##combo = Combobox(window)
##select = StringVar()
##combo['values'] = ("select","RCB","CSK","MI","KKR","SRH")
##combo.current(0)
##combo.grid(column=0,row=1)
##def click():
##    print(combo.get())
##
##btn = Button(window,text="click me",command=click)
##btn.grid(column=1,row=1)

##from tkinter import *
##window = Tk()
##window.title("welcome to tkinter")
##window.geometry('500x400')
##
##
##menu = StringVar()
##menu.set("select team")
##drop = OptionMenu(window,menu,'CSK','GT','RCB','KBFC')
##drop.grid(column=1,row=20)
##drop.pack()

from tkinter import *
window = Tk()
window.title("welcome to tkinter")
window.geometry('500x400')
chk = BooleanVar()
chk.set(0)
check = Checkbutton(window,text="cricket",va=chk)
check.grid(column=0,row=0)
chk1 = BooleanVar()
chk1.set(0)
check = Checkbutton(window,text="football",va=chk1)
check.grid(column=0,row=1)
chk2 = BooleanVar()
chk2.set(1)
check = Checkbutton(window,text = "games",va=chk2)
check.grid(column=0,row=2)
chk3 = BooleanVar()
chk3.set(0)
check = Checkbutton(window,text = "Movies",va=chk3)
check.grid(column=0,row=3)
