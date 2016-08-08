from Tkinter import *
import Tkinter, tkFileDialog, os,sys
from distutils.core import setup
import py2exe

root = Tkinter.Tk()
dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

def extReplace():
  global e1
  global e2
  folder = dirname
  oldExt = e1.get()
  newExt = e2.get()
  for filename in os.listdir(folder):
    print filename
    oldbase = os.path.splitext(filename)

    infilename = os.path.join(folder,filename)
    oldbase = os.path.splitext(filename)
    newname = infilename.replace(oldExt, newExt)
    output = os.rename(infilename, newname)

label1 = Label( root, text="Old File Ext")
e1 = Entry(root, bd =5)
label2 = Label( root, text="New File Ext")
e2 = Entry(root, bd =5)

label1.pack()
e1.pack()
label2.pack()
e2.pack()
submit = Button(root, text ="Submit", command = extReplace)
submit.pack(side =BOTTOM)    
    
if len(dirname ) > 0:
  
  root.mainloop()