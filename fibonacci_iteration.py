# A positive number N is given to you and You need to calculate Nth Number in Fibonacci Series.

n=int(input("Enter the term you wnat to print ? "))

def fibb(n):
    first=0
    second=1
    if n==1:
        return first
    elif n==2:
        return second
    else:
        i=0
        while(i<n-2):
            temp=first+second
            first=second
            second=temp
            i+=1
        return temp


if(__name__=="__main__"):
        if n>=0:
            print(fibb(n))
