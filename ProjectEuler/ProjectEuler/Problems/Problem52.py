#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits

def HasSameDigits(num1, num2):
	dict = {}
	val = num1

	while(val > 0):	
		d = num1 % 10
		num1 /= 10
		if(dict.has_key(d)):
			dict[d] += 1
		else:
			dict[d] = 1
	val = num2
	
	while(val > 0):
		d = num2 % 10
		num2 /= 10
		dict[d]