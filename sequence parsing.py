#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     22-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Bio
from
def main():
    for seq_record in SeqIO.parse("","fasta"):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))

if __name__ == '__main__':
    main()
