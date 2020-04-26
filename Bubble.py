
def Bubble(list):
    
    for number in range(len(list)-1,0,-1):
        for internal in range(number):
            if list[internal] > list[internal+1]:
                list[internal],list[internal+1]=  list[internal+1],list[internal]
        
        


    
    
list  = [4,2,7,9,1,8,5,3]
Bubble(list)

print(list)
    