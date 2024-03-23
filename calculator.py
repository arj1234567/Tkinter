from tkinter import *
exp =''
def press(num):
    global exp
    exp = exp + str(num)
    print("expression=",exp)
    p =equation.set(exp)

def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp=''
    except:
        equation.set('error')
        exp=''

def clear():
    global exp
    exp =''
    equation.set("")
    
window=Tk()
window.title("wlcome to tkinter")
window.geometry('800x600')
equation = StringVar()
textbox = Entry(window,width=80,textvariable=equation)
textbox.grid(columnspan=4,ipadx=0)

b1 = Button(window,text='1',bg="red",fg="white",command =lambda:press(1),width=5,height=2)
b1.grid(column=0,row=2)
b2 = Button(window,text='2',bg="red",fg="white",command =lambda:press(2),width=5,height=2)
b2.grid(column=1,row=2)
b3 = Button(window,text='3',bg="red",fg="white",command =lambda:press(3),width=5,height=2)
b3.grid(column=2,row=2)
b4 = Button(window,text='4',bg="red",fg="white",command =lambda:press(4),width=5,height=2)
b4.grid(column=0,row=3)
b5 = Button(window,text='5',bg="red",fg="white",command =lambda:press(5),width=5,height=2)
b5.grid(column=1,row=3)
b6 = Button(window,text='6',bg="red",fg="white",command =lambda:press(6),width=5,height=2)
b6.grid(column=2,row=3)
b7 = Button(window,text='7',bg="red",fg="white",command =lambda:press(7),width=5,height=2)
b7.grid(column=0,row=4)
b8 = Button(window,text='8',bg="red",fg="white",command =lambda:press(8),width=5,height=2)
b8.grid(column=1,row=4)
b9 = Button(window,text='9',bg="red",fg="white",command =lambda:press(9),width=5,height=2)
b9.grid(column=2,row=4)

b10 = Button(window,text='+',bg="red",fg="white",command =lambda:press('+'),width=5,height=2)
b10.grid(column=3,row=2)
b11 = Button(window,text='-',bg="red",fg="white",command =lambda:press('-'),width=5,height=2)
b11.grid(column=3,row=3)
b12 = Button(window,text='*',bg="red",fg="white",command =lambda:press('*'),width=5,height=2)
b12.grid(column=3,row=4)

a1=Button(window,text='0',bg="red",fg="white",command=lambda:press(0),width=5,height=2)
a1.grid(column=0,row=5)
a2=Button(window,text='clear',bg="red",fg="white",command=clear,width=5,height=2)
a2.grid(column=1,row=5)
a3=Button(window,text='=',bg="red",fg="white",command=equalpress,width=5,height=2)
a3.grid(column=2,row=5)
a1=Button(window,text='/',bg="red",fg="white",command=lambda:press('/'),width=5,height=2)
a1.grid(column=3,row=5)

window.mainloop()
