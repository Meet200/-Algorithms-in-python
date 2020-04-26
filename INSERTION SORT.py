def insertion(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i-1
        while(j>=0 and temp < a[j]):
           a[j+1] = a[j]
           j = j-1
           a[j+1]= temp
           
    
    
    
a = [1,7,99,3,0,2,34,12]
insertion(a)
print(a)
        
