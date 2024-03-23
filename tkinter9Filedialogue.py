from tkinter import * 
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter.messagebox import showinfo

window=Tk()
window.title('welcome to python')
window.geometry('350x200')
##file=filedialog.askopenfilename()



def select_files():
    filetypes =(('text files', '*.txt'),('All files', '*.*'))
    
    filenames = filedialog.askopenfilenames(title='Open files',initialdir='/', filetypes=filetypes)
        
    showinfo(title='Selected Files', message=filenames)      

open_button =Button(window,text='Open Files',command=select_files)
   

open_button.pack(expand=True)
window.mainloop()
