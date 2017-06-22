#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     22-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("Enter the limits")
    a=int(raw_input())
    b=int(raw_input())
    for i in range(a,b):
        if(i%2==0):
            print("%d"%i)


if __name__ == '__main__':
    main()
