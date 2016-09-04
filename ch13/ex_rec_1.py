# A recursive function to compute the factorial of a number.
# In mathematics, the factorial of a non-negative integer n, denoted by n!,
# is the product of all positive integers less than or equal to n.
# For example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120.

def computeFactorial(number):
    if number < 0:
        return None

    if number == 0:
        return 1
    
    if number == 1:
        return number
    else:
        return number * computeFactorial(number - 1)

print(computeFactorial(-5))
