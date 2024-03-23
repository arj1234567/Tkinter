##from tkinter import *
##from tkinter.ttk import Progressbar
##window=Tk()
##window.title("welcome to tkinter")
##window.geometry("500x400")
##bar = Progressbar(window,length=100)
##bar.grid(column=0,row=0)
##bar['value'] = 80
##


from tkinter import *
from tkinter.ttk import Progressbar
window=Tk()
window.title("welcome to tkinter")
window.geometry("500x400")
pb1 = Progressbar(window,length=100,orient = HORIZONTAL,mode="determinate")
pb1.grid(column=0,row=0)
pb1.start()


##from tkinter import *
##from tkinter.ttk import Progressbar
##window=Tk()
##window.title("welcome to tkinter")
##window.geometry("500x400")
##pb1 = Progressbar(window,length=100,orient=HORIZONTAL,mode="indeterminate")
##pb1.grid(column=0,row=0)
##pb1.start()
