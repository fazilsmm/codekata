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
    a = int(raw_input("Enter the number"))
    flag = 0
    for i in range(2,a-1):
        if(a%i==0):
            flag=1
    if(flag==0):
        print("The number is prime")
    else:
        print("The number is not prime")




if __name__ == '__main__':
    main()
