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
    n = int(input("Enter the limit"))
    c = 0
    b = 1
    a = 0
    while (a != n):
        c = c + b
        b +=1
        a +=1
    print("The sum is %d"%c)
if __name__ == '__main__':
    main()
