# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):       #checks if a number is a palindrome by converting
    return str(num) == str(num)[::-1] #to a string, inverting, and comparing

def largest(low,high):  
    z = 0
    for x in range(high, low, -1): #iterates backwards from high to low
        for y in range (high, low, -1): 
            if isPalindrome(x*y): #checks if product is palindrome
                if (x*y) > z: #checks if it is larger than all other found palindromes
                    z = x*y
                    x1 = x
                    y1 = y
    print(x1, y1)
    return z

print(largest(100,999))  
