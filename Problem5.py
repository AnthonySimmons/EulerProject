
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def IsCommonProduct(nums, val):
	isCommon = True
	for num in nums:
		if(val % num != 0):
			isCommon = False
			break
	return isCommon


def SmallestCommonProduct(nums):
	
	minVal = min(nums)
	maxVal = max(nums)
	product = maxVal
	print(str(minVal))
	while(IsCommonProduct(nums, product) == False):		
		product += maxVal
	return product
	
	
smallestCommonProduct = SmallestCommonProduct(range(1, 21))

print("Smallest Common Product: \n" + str(smallestCommonProduct))