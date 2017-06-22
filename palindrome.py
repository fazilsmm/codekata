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
    n = int(raw_input("Enter the number"))
    m = n
    r = 0
    while(n>0):
        r = r * 10
        r = r + n%10
        n = n/10
    if(r==m):
        print("The number is palindrome")
    else:
        print("The number is not palindrome")



if __name__ == '__main__':
    main()
