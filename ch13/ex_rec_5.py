# A recursive function to compute the Fibonacci sequence. 

def fibonacci(limit):
    """Takes a positive integer (limit) as an argument, and returns the \
       Fibonacci sequence as a list, with values up to, but not including limit."""
           
    if limit <= 2:
        return 1
    else:
        return fibonacci(limit - 1) + fibonacci(limit - 2)

print(fibonacci(9))
    
