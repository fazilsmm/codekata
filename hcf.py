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
    print("enter two numbers")
    try:
        a = int(input("Please enter a number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        exit()
    try:
        b = int(input("Please enter a number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        exit()
    while (b != 0):
            c = b
            b = a%b
            a = c
    hcf = a
    print("The HCF is %d"%hcf )

if __name__ == '__main__':
    main()
