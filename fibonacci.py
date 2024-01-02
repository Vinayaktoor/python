a = int(input("series till :"))
i=3
n1=0
n2=1
if a==2:
   print(n1)
   print(n2)
elif a==1:
     print(n1)  
if a>=3:
    print(n1)
    print(n2)
    while i<=a:
         temp=n1+n2
         n1=n2
         n2=temp
         print(temp)
         i =i+1