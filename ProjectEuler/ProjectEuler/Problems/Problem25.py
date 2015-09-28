#What is the index of the first term in the 
#Fibonacci sequence to contain 1000 digits?

def FibonacciIndexByDigits(numDigits):
	prev = 1
	cur = 1
	i = 0
	while(True):
		cur = prev + cur
		prev = cur
		fibStr = str(cur)
		if(len(fibStr) >= numDigits):
			return i, cur
		i += 1
		
def Solve():
    index, val = FibonacciIndexByDigits(1000)
    print("First 1000 Digit Fibonacci Index : Value = \n" + str(index) + " : " + str(val))
    return index