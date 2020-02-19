#A positive number N is given to you and You need to calculate its factorial.

n=int(input("Enter a number "))

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

if(__name__=="__main__"):
    if(n>0):
         print("Factorial of number is : ",fact(n))
