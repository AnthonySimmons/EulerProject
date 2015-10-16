
#n! means n × (n ? 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

def Factorial(num):
    fact = num
    for i in reversed(range(1, num)):
        fact *= i
    return fact

def SumOfDigits(num):
    sum = 0
    numStr = str(num)
    for c in numStr:
        sum += int(c)
    return sum

def Solve():
    num = 100
    fact = Factorial(num)
    sum = SumOfDigits(fact)
    print("Factorial: {}, Sum: {}".format(fact, sum))
    return sum