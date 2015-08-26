from tkinter import *
from tkinter.filedialog import *
import fileinput
import codecs

##def _open():
##     op = askopenfilename()
##     for l in fileinput.input(op):
##          txt.insert(END,l)

def _new():
    # Clear the text
    txt.delete(1.0, END)

def _open():
    op = askopenfilename(filetypes=[('text files', '.txt'),('obj files', '.obj'),('zip files', '.zip')]) #ТЕСТОВЫЕ РАЗРЕШЕНИЯ
    filee = codecs.open(op,"r","utf-8")
    file_lines = filee.read()
    for l in file_lines:
        txt.insert(END,l)

def _saveAs():
    # Returns the saved file
    file = asksaveasfile(mode='w',filetypes=[('text files', '.txt'),('zip files', '.zip')])   #ТЕСТОВЫЕ РАЗРЕШЕНИЯ
    textoutput = txt.get(1.0, END) # Gets all the text in the field
    file.write(textoutput.rstrip()) # With blank perameters, this cuts off all whitespace after a line.
    file.write("\n") # Then we add a newline character.

def _saveAsCoded():
    # Returns the saved coded
    file = asksaveasfile(mode='w',filetypes=[('text files', '.txt'),('obj files', '.obj'),('zip files', '.zip')]) #ТЕСТОВЫЕ РАЗРЕШЕНИЯ
    textoutput = txt.get(1.0, END) # Gets all the text in the field
    file.write(textoutput.rstrip()) # With blank perameters, this cuts off all whitespace after a line.
    file.write("\n") # Then we add a newline character.

def close_win():
     root.destroy()

def about():
     win = Toplevel(root)
     lab = Label(win,text='''Alas, my love, you do me wrong,

To cast me off discourteously.

For I have loved you well and long,

Delighting in your company.''')
     lab.pack()


root = Tk()

m = Menu(root)
root.config(menu=m)

tm = Menu(m)
m.add_cascade(label="Text",menu=tm)
tm.add_command(label="New",command=_new)
tm.add_command(label="Open",command=_open)
tm.add_command(label="Save text",command=_saveAs)
tm.add_command(label="Save coded",command=_saveAsCoded)
tm.add_command(label="Exit",command=close_win)


km = Menu(m)
m.add_cascade(label="Key",menu=km)
km.add_command(label="Open key source",command="")
km.add_command(label="Open key",command="")
km.add_command(label="Generate key",command="")
km.add_command(label="Save key",command="")

gm = Menu(m)
m.add_cascade(label='Coding',menu=gm)
gm.add_command(label="Coding",command="")
gm.add_command(label="Decoding",command="")


m.add_command(label="About",command=about)


txt = Text(root,width=40,height=15,font="12")
txt.pack(expand=YES, fill=BOTH)

root.mainloop()