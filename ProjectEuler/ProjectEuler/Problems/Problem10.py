import sys
from Utilities import Prime
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.


def IsPrime(num):
    return Prime.IsPrime(num)

def SumOfPrimes(max):
    sum = 2
    for i in range(3, max):
        if(IsPrime(i) == True):
            sum += i
    return sum

def Solve():
    max = 2000000
    sum = SumOfPrimes(max)
    return sum
