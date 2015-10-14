import sys
import math
from Utilities import Prime

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def LargestPrimeFactor(num):
    max = 1
    sq = int(math.sqrt(num))
    factors = range(2, sq+1)
    for i in factors:
        if(num % i == 0):
            if(Prime.IsPrime(i)):
                if(i > max):
                    max = i
            dividend = int(num / i)
            if(Prime.IsPrime(dividend)):   
                if(dividend > max):
                    max = dividend
                
    return max

def Solve():
    num = 600851475143
    lpf = LargestPrimeFactor(num)
    print("Largest Prime Factor: " + str(lpf))
    return lpf