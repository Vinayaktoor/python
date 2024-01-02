try :
    n = int(input("enter value of n:"))
except  Exception as e:
    print("wrong input:",e)
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")         
else :
    print("n is zero")
           