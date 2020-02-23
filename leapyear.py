#An Year as input is given and You need to check that it's leap year or not.

year=int(input("Enrer year "))

if year%100==0 and year%400:
    print("leap year")
elif year%100!=0 and year%4==0:
    print("leap year")
else:
    print("Not a leap year")
