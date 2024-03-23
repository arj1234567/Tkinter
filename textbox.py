from tkinter import *
window=Tk()
window.title("welcome to tkinter")
window.geometry('550x400')
lbl=Label(window,text="hai")
lbl.grid(column=0,row=0)
txt=Entry(window,width=10)
txt.grid(column=0,row=1)

def click():
    res="hai from "+txt.get()
    lbl.configure(text=res)

btn=Button(window,text="click me",command=click,bg="black",fg="white")
btn.grid(column=1,row=1)
