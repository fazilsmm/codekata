#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     20-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("Enter 3 numbers")
    a = int(input())
    b = int(input())
    c = int(input())
    if (a>b and a>c):
        print ("%d is greater"%a)
    elif (b>a and b>c):
        print ("%d is graeter"%b)
    else:
        print ("%d is greater"%c)

if __name__ == '__main__':
    main()
