from numpy import *

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return a*fibonacci(n-2)+b*fibonacci(n-1)

n= float(input("entre n"))
a=b=1
print("le",n,"ieme nombre de fibonacci est",fibonacci(n))