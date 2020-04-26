print("Enter text")
text = input ()
print("Enter Pattern ")
pattern = input()
x = len(text)
y = len(pattern)
d = 256
sump=0
sumt=0
for i in range(y):
	sump = sump+(ord(pattern[i])*(d**(y-i-1)))
print(sump)

for i in range(y):
	sumt = sumt+(ord(text[i])*(d**(y-i-1)))
	
print(sumt)
if(sump == sumt):
	print("Same !!")
for i in range(y,x):
	sumt =(sumt-(ord(text[i-y])*(d**(y-1))))*d+ord(text[i])
	
	if(sump == sumt):
		print("same!!!")
		
	else:
		print("Not Match ##")