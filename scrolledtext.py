from tkinter import *
from tkinter import scrolledtext
window=Tk()
window.title("welcome to tkinter")
window.geometry("500x400")
txt = scrolledtext.ScrolledText(window,width=10,height=7)
txt.grid(column=0,row=0)
txt.insert(INSERT,"Your text goes here")
def click():
    print(txt.get('1.0','end'))
btn = Button(window,text="click me",command = click)
btn.grid(column=0,row=1)

