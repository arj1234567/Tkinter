from tkinter import *


expression=''
def press(num):
    global expression
    expression=expression+str(num)
    print('expression=',expression)
    p=equation.set(expression)

def equalpress():
    try:
        global expression      
        total=str(eval(expression))
        print('total=',total)
        equation.set(total)
        expression=''
    except:
        equation.set('error')
        expression=''
def clear():
    global expression
    expression=''
    equation.set("")


window =Tk()
window.title('welcome to python')
window.geometry('500x300')
equation=StringVar()
textbox=Entry(window,width=60,textvariable=equation)
textbox.grid(columnspan=4,ipadx=0)


b1=Button(window,text='1',bg='black',fg='white',command=lambda:press(1),width=7,height=1)
b1.grid(row=2,column=0)
b2=Button(window,text='2',bg='black',fg='white',command=lambda:press(2),width=7,height=1)
b2.grid(row=2,column=1)
b3=Button(window,text='3',bg='black',fg='white',command=lambda:press(3),width=7,height=1)
b3.grid(row=2,column=2)
b4=Button(window,text='4',bg='black',fg='white',command=lambda:press(4),width=7,height=1)
b4.grid(row=3,column=0)
b5=Button(window,text='5',bg='black',fg='white',command=lambda:press(5),width=7,height=1)
b5.grid(row=3,column=1)
b6=Button(window,text='6',bg='black',fg='white',command=lambda:press(6),width=7,height=1)
b6.grid(row=3,column=2)
b7=Button(window,text='7',bg='black',fg='white',command=lambda:press(7),width=7,height=1)
b7.grid(row=4,column=0)
b8=Button(window,text='8',bg='black',fg='white',command=lambda:press(8),width=7,height=1)
b8.grid(row=4,column=1)
b9=Button(window,text='9',bg='black',fg='white',command=lambda:press(9),width=7,height=1)
b9.grid(row=4,column=2)

b10=Button(window,text='+',bg='black',fg='white',command=lambda:press('+'),width=7,height=1)
b10.grid(row=2,column=3)
b11=Button(window,text='-',bg='black',fg='white',command=lambda:press('-'),width=7,height=1)
b11.grid(row=3,column=3)
b12=Button(window,text='*',bg='black',fg='white',command=lambda:press('*'),width=7,height=1)
b12.grid(row=4,column=3)

a1=Button(window,text='0',bg='black',fg='white',command=lambda:press(0),width=7,height=1)
a1.grid(row=5,column=0)
a2=Button(window,text='clear',bg='black',fg='white',command=clear,width=7,height=1)
a2.grid(row=5,column=1)
a3=Button(window,text='=',bg='black',fg='white',command=equalpress,width=7,height=1)
a3.grid(row=5,column=2)
a4=Button(window,text='/',bg='black',fg='white',command=lambda:press('/'),width=7,height=1)
a4.grid(row=5,column=3)

window.mainloop()
