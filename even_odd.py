# A positive number N is given to you and You need to check Whether a Number is Even or Odd.

num=int(input("Enter number "))

def even_odd(n):
    if (int(num/2)*2)!=num:
        return False
    else:
        return True


if(__name__=="__main__"):
    if num>0:
        b=even_odd(num)
        if b==True:
            print("Even")
        else:
            print("Odd")
