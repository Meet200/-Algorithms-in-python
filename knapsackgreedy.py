def  fractionkp(amount,weight,W):
	ratio = []
	for i in range(len(amount)):
		ratio.append(int(amount[i]/weight[i]))
	print(ratio)
	index = sorted(range(len(ratio)),key = lambda k : ratio[k])
	index.reverse() 
	print(index)
	fractional = [0 for i in range(len(amount))]
	maxprice = 0
	for i in range(len(amount)):
		if W>=weight[index[i]]:
			fractional[index[i]] = 1
			maxprice +=amount[index[i]]
			W-=weight[index[i]]
		
	return maxprice

	









amount = [60,50,120]
weight = [20,10,30]
W = 50
out = fractionkp(amount,weight,W)
print(out)