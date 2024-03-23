from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import messagebox
window=Tk()
window.title("welcome to tkinter")
window.geometry('350x200')
##file = filedialog.askopenfilename()
def select_file():
    filetype = (('All files','*.*'),('text files','*.txt'))
    filenames = filedialog.askopenfilenames(title="Open",initialdir='/',filetypes=filetype)
    messagebox.showinfo(title="Select files",message =filenames)
btn = Button(window,text="Open",command=select_file)
btn.pack(expand=True)
window.mainloop()
    
