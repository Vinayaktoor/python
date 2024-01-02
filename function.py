class solution:
    def paladrome(self,num):
        a = str(num)
        a = a[::-1]
        if int(a)==num:
            print("the given no. is a paldrome",num)
class solution2(solution) :
     def paladrome(self, num):
         i=1
         num_str=str(num)
         a = len(str(num))
         if a%2 != 0:
            while i<a:
                if num_str[i]==num_str[a-i]:
                    continue
                if i == a-i:
                        continue
                if num_str[i]!=num_str[a-i]:
                    print("the given no. is not a paladrome")
                    break
            else:
                print("given no.is a paladrom")         
         else:
             print("given no.cannot be a paladome")                
sol1 = solution()
sol2 = solution2()
paladrome_mum = int(input("enter a num :"))
sol1.paladrome(paladrome_mum)
sol2.paladrome(paladrome_mum)                  
                
                
        
    