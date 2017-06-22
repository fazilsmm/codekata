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
import Bio
from Bio.Seq import Seq

def main():
    my_seq = Seq("GTGGGTAGGTA")
    print(my_seq)
    print(my_seq.complement())


main()
