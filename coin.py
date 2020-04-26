def coinchain(coin , amount):
	a = [0 for i in  range(amount+1)]
	a[0] = 1
	for coi in range (len(coin)):
		for i in range(coin[coi],len(a)):
			a[i] = a[i-coin[coi]]+a[i]
			print(a[i],i)
	a[0] = 0
	return a
	

amount = 9
coin = [1,2,5]
out = coinchain(coin,amount)
c = [0,1,2,3,4,5,6,7,8,9]
print("Values ==>               ", end =" ")
print(c)
print("Possible Combination ==> ", end =" ")
print(out)





