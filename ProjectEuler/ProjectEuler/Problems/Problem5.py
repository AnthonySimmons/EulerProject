

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
	nums.sort(reverse = True)
	minVal = min(nums)
	maxVal = max(nums)
	product = maxVal
	while(IsCommonProduct(nums, product) == False):		
		product += maxVal
	return product
	
	
def Solve():
    nums = list(range(1, 21))
    smallestCommonProduct = SmallestCommonProduct(nums)
    print("Smallest Common Product: \n" + str(smallestCommonProduct))
    return smallestCommonProduct