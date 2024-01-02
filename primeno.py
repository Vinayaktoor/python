a = int(input("enter value of a:"))
l = [2,3,4,5,6,7,8,9]
for i in l:
    if a==0:
        print("neither prime nor prime{zero input} ")
        break
    if i/a==1:
        continue
    if a%i==0:
       print(a,"is not a prime no.")
       break
    else :
        print(a,"is a prime no.")
        break