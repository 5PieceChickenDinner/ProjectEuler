#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#we can see that the 6th prime is 13.
#What is the 10001st prime number?


import math

def isPrime(num): #returns True if argument is prime, False if it is not
    for x in range(2, int(math.sqrt(num))+1):
        if num%x==0:
            return False
    return True
        
def primeCount(x): #returns the xth prime number
    i = 0
    n = 1
    while i < x:
        n += 1
        if isPrime(n):
            i = i + 1
    return n

print(primeCount(10001))
