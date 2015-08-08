

#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


def SumOfSquaresInSequence(sequence):
	sum = 0
	for num in sequence:
		power = pow(num, num)
		sum += power
	return sum
		
sequence = range(1, 1000)
sum = SumOfSquaresInSequence(sequence)

def LastDigits(value, numDigits):
	digits = []	
	for i in range(numDigits):
		d = value % 10
		value = int(value / 10);
		digits.add(d)
	return digits

#lastTenDigits = LastDigits(sum, 10)
 
sumStr = str(sum)
print("Sum: " + sumStr)
print("Last Ten Digits: " + sumStr[-10:])