#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     22-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
tempdir = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
if len(tempdir) > 0:
    print "You chose %s" % tempdir
