#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     21-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    myfile = open("F:\\courses\\python\\text.txt","w+")
    print(myfile.read())
    myfile.write("hello1")
if __name__ == '__main__':
    main()
