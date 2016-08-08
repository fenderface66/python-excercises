import Tkinter, tkFileDialog, os,sys
from distutils.core import setup
import py2exe

root = Tkinter.Tk()
dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
if len(dirname ) > 0:
  folder = dirname
  print "You chose %s" % folder
  oldExt = raw_input("What extension type would you like to replace?")
  newExt = raw_input("What would you like the new extension to be?")
  for filename in os.listdir(folder):
    print filename
    oldbase = os.path.splitext(filename)
  
    infilename = os.path.join(folder,filename)
    oldbase = os.path.splitext(filename)
    newname = infilename.replace(oldExt, newExt)
    output = os.rename(infilename, newname)


setup(console=['test.py'])