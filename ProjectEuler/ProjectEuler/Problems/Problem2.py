﻿#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def FibonacciEvenSum(start1, start2, maxValue):
	x = start1
	y = start2
	evenSum = 0
	val = 0
	while(val <= maxValue):
		val = x + y
		x = y
		y = val
		if(val < 100): 
			print (str(val))
		if(val % 2 == 0):
			evenSum += val			
	
	return evenSum
	
def Solve():
    fibEvenSum = FibonacciEvenSum(0, 1, 4000000)
    print ("Sum of Even Fibonnaci Numbers less than 4,000,000: \n" + str(fibEvenSum))
    return fibEvenSum