

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def SumOfSquares(nums):
	sum = 0
	for num in nums:
		sum += num * num
	return sum
	
def SquareOfSum(nums):
	sumVal = sum(nums)
	return sumVal * sumVal
	
def Solve():
    nums = range(1, 101)

    sumOfSquares = SumOfSquares(nums)
    squareOfSums = SquareOfSum(nums)

    diff =  squareOfSums - sumOfSquares;

    print("Sum Of Squares: " + str(sumOfSquares))
    print("Square Of Sums: " + str(squareOfSums))
    print("Difference: " + str(diff))
    return diff