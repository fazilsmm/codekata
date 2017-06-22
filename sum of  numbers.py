#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     21-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    t=[]
    a=int(raw_input("Enter the number of terms:"))
    b=0
    c=0
    for a in range(0,a):
       b = int(raw_input("Enter the value"))
       t.append(b)
       c +=b
    print(c)



if __name__ == '__main__':
    main()
