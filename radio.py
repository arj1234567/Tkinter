from tkinter import *
window=Tk()
window.title("welcome to tkinter")
window.geometry("500x400")
selected = StringVar()
radio = Radiobutton(window,text="male",value="male",variable=selected)
radio.grid(column=0,row=0)
radio = Radiobutton(window,text="female",value="female",variable=selected)
radio.grid(column=1,row=0)
def submit():
    print(selected.get())
btn = Button(window,text="submit",command=submit)
btn.grid(column=0,row=1)
