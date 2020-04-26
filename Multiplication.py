x= int(input("Enter The Number1 : "))
y= int(input("Enter The Number2: "))



def karatsuba(x,y):
    if (x<10 or y<10):
        return x*y
    m = max(len(str(x)),len(str(y)))
    if m%2 !=0:
        m = m-1
    
    a,b = divmod(x,10**int(m/2))
    c,d = divmod(y,10**int(m/2))
    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba((a+b),(c+d))-ac-bd
    
    return((ac*(10**m))+bd+((ad_bc)*(10**int(m/2))))
    
    
    
    
    
 

karatsuba(x,y) 
    
ans = karatsuba(x,y) 
    
print(ans)