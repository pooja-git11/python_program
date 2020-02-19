#A positive number N is given to you and You need to calculate its factorial.



def fact(n):
    fact=1
    i=n
    while i!=0:
        fact*=i
        i-=1
    return fact

if(__name__=="__main__"):
    num = int(input("Enter a number "))
    if num>-1:
        print("Factorial is : ",fact(num))

