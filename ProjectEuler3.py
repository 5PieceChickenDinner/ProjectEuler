#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143?

from timeit import default_timer

n = 600851475143

start1 = default_timer()

i = 2
while i*i <= n:        #Only need to check up to sqrt of n
    while n % i == 0:  
        if n == i:     #If n is a power of i, this ensures that i will be returned
            break
        n = n / i      #Will divide by i until i is no longer a factor of n
        
    i += 1
end1 = default_timer()

print(n)

start2 = default_timer()

i = 3                  #Start at 3 since n isn't even
while i*i <= n:        #Only need to check up to sqrt of n
    while n % i == 0:  
        if n == i:     #If n is a power of i, this ensures that i will be returned
            break
        n = n / i      #Will divide by i until i is no longer a factor of n
        
    i += 2             #Iterate by 2 since no even numbers will be factors
end2 = default_timer()

print(n)

time1 = end1 - start1
time2 = end2 - start2

print('Second method takes ' + str(time2/time1) + ' the time of first method.')
