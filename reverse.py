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
    a = int(input("Enter the number"))
    r = 0
    while(a>0):
        r = r*10
        r = r + (a % 10)
        a = a/10
    print("the Reverse number is %d"%r)

if __name__ == '__main__':
    main()
