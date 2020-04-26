


def Selection(y):
    for i in range(len(y)):
        
        index = i
        j = i+1
   
        for j  in  range(len(y)):
            if y[index]>y[j]:
               
                index = j
        y[i],y[index] = y[index],y[i]
    return y

    
    
    
    
    
y = [1,5,3,8,5,0]
Selection(y)   
print(Selection(y))
        