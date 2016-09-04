# Sum all the elements in a list up to but not including the first even number.

def sumUntilEven(lst):
    total = 0
    
    for i in lst:
        if i % 2 == 0:
            break
        total = total + i
        
    return total
    
print(sumUntilEven([1,3,3,4,5]))
