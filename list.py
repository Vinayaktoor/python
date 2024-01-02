l1 = [1,2,3,4,2,5,6,7,43,577,54,32]
print(l1)
l1=list(set(l1))
print(l1)
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