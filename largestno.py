a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = int(input("enter value of c:")) 
if a > b:
    if a>c:
        print("a is biggest no.")
    if c>a:
        print("c is the biggest no.")
    if a>c>b:
        print("c is second biggest no. ")
    if c>a:
        print("a is second biggest no.")        
            
else :
    if b>c:
        print("b ids the biggest no.")
    if c>b:
        print("c is the biggest no.")                
    if b>c>a:
        print("c is second biggest no.")
    if a>c:
        print("a is second biggest no.")    