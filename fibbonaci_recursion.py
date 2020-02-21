# A positive number N is given to you and You need to calculate Nth Number in Fibonacci Series.

n=int(input("Enter the term you wnat to print ? "))

def fibb(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)



if(__name__=="__main__"):
    print(fibb(n))
