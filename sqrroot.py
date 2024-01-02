try :
   n = int(input("eneter no."))
except Exception as e :
    print("wrong input:",e)
s = n**(1/2)
print("square root of a given no. is ",s,type(s))   
       