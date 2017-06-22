#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     21-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    str1 = str(raw_input("Enter:"))
    '''print(len(a))'''

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    print(rstr1)



if __name__ == '__main__':
    main()
