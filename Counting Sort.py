def cs(s):
    arr = [0 for i in range(256)]  # to make the Array of size 256 Initialay Value 0
    for i in range (len(s)):
        arr[ord(s[i])] = arr[ord(s[i])]+1
    output = ''
    for i in range(256):
        output += (arr[i]*(chr(i)))
    print(output)
s = 'MEETTHON'
cs(s) 
  
    
