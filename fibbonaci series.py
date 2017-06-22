#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fazil Smm
#
# Created:     19-06-2017
# Copyright:   (c) Fazil Smm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def fib():
    lim = int(input("Enter the number of elements in fibonacci series:"))
    val1 = 0
    val2 = 1
    print(val1,val2)
    for i in range(0,lim):
        val3 = val1 + val2
        print (val3)
        val1 = val2
        val2 = val3
fib()

