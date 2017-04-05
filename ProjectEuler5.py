#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by
#all of the numbers from 1 to 20?

def factor(num): #returns an array of prime factorization of num
    a = 2
    factors = []
    while a*a <= num:
        while num % a == 0:
            if num == a:
                break
            factors.append(a)
            num /= a
        a += 1
    factors.append(num)
    return factors

def Count(n): #initializes an array that will count prime factors
    return [0] * (n+1) 

def createNumber(num): #returns a number that is evenly divisible by all integers 1-num
    factorCount = Count(num)
    for i in range(2,num+1):
        array1 = factor(i)
        for j in range(2, i+1):
            if array1.count(j) > factorCount[j]:
                factorCount[j] = array1.count(j)
    product = 1
    for i in range(2,num+1):
        if factorCount[i] > 0:
            product = product * (i ** factorCount[i])
    return product

print(createNumber(20))
