

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


def IsPalindrome(val):
	i = 0
	j = len(val) - 1
	isPalindrome = True
	while(i < j):
		if(val[i] != val[j]):
			isPalindrome = False
			break
		i += 1
		j -= 1
	return isPalindrome

def LargestPalindrome():
	largest = 0
	upperBound = 999
	lowerBound = 100
	maxVal = 0
	maxI = 0
	maxJ = 0
	for i in range(upperBound, lowerBound, -1):
		for j in range(upperBound, lowerBound, -1):
			
			product = i * j
			if(IsPalindrome(str(product))):
				largest = product
				if(maxVal < largest):
					maxVal = largest
					maxI = i
					maxJ = j
	return maxI, maxJ, maxVal
	
def Solve():
    i, j, largestPalindrome = LargestPalindrome()
    print("Largest Palindrome that is a Product of 3-digit numbers: \n" + str(i) + " * " + str(j) + " = " + str(largestPalindrome))
    return largestPalindrome