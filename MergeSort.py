def mergesort(list):
    if len(list)>1:
        mid = int(len(list)/2)
        lefthalf = list[:mid]
        righthalf = list[mid :]
        
        mergesort(lefthalf)
        mergesort(righthalf)

        
        i=j=k=0
        while i<len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i+=1
            else:
                list[k] = righthalf[j]
                j+=1;
            k+=1 
            
        while i<len(lefthalf):
            list[k] = lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            list[k] = righthalf[j]
            j+=1
            k+=1
            

list=[52,-5,-52,1,-46]
mergesort(list)
print(list)