i = 0
l1 = []
n = int(input("enter length of list:"))
while i<n:
    ele=int(input ("enter elements of the list:" ))
    l1.append(ele)
    i=i+1
l1 = list(set(l1))
i=0
n=len(l1)
temp=int
while i<n-1:
    if int(l1[i])>int(l1[i+1]):
        temp=l1[i]
        l1[i]=l1[i+1]
        l1[i+1]=temp
    i=i+1      
print(l1)          
            