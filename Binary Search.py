def bs(arr,l,r,key):
    if r>=l:
        mid=int((l+r)/2)
        if arr[mid]==key :
            return mid
        elif arr[mid] > key:
            return bs(arr,l,mid-1,key)
        else:
            return bs(arr,mid+1,r,key)
  
    else:
        return -1
    

arr= [-1,-2 ,-3,0,1,2]
x = -1
catch = bs(arr,0,len(arr)-1,x)
if (catch==-1):
    print("\n\n\t  Element Not Found")
else:
    print("Element Found At ",catch)