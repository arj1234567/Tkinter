from tkinter import *
from tkinter import Spinbox
window=Tk()
window.title("welcome to tkinter")
window.geometry("500x400")
box = Spinbox(window,from_=1,to=10,width=12)
box.grid(column=0,row=0)
def click():
    print(box.get())
btn = Button(window,text="click",command=click)
btn.grid(column=1,row=1)
