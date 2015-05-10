def addArrays(array1, array2):
	#from stackoverflow, zip function adds values in two arrays of same length
	#returning array C for value i and the total number of coins for value i
	return ([x + y for x, y in zip(array1, array2)], array1[1] + array2[1])

def changeslow(array, K):
	#If there is a K-cent coin, then that one coin is the minimum
	if array._contains_(K):
		C = [0] * len(array) #Initialize an array of 0s the length of the array 
		C[array.index(K)] = 1 #increase the count of K-cent coin
		return [C, 1] #return C array and number of coins (1)
	else:
		minimum = None
		for i in array:
			if not i < K:
				break
			numCoins1 = changeslow(array, i)
			numCoins2 = changeslow(array, K-i)
			totalCoins = addArrays(numCoins1, numCoins2)

			if totalCoins[1] < minimum[1]:
				minimum = totalCoins
return minimum #minimum[0] returns array C and minimum[1] returns total number of coins
				
	
		
