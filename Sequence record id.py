#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     22-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *
import tkFileDialog
import Bio
from Bio import SeqIO
import sys
if sys.version_info[0] < 3:
   import Tkinter as Tk
else:
   import tkinter as Tk


def browse_file():

    fname = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.fasta"), ("All files", "*")))
    print fname
    for seq_record in SeqIO.parse(fname,"fasta"):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))

root = Tk.Tk()
root.wm_title("Browser")
broButton = Tk.Button(master = root, text = 'Browse', width = 6, command=browse_file)
broButton.pack(side=Tk.LEFT, padx = 2, pady=2)

Tk.mainloop()



