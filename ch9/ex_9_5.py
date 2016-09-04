# Write a Python function that will take a the list of 100 random
# integers between 0 and 1000 and return the maximum value. (Note:
# there is a builtin function named max but pretend you cannot use it.)

import random

def create_list(num, limit):
    """create a list containing num random integers from 0 to limit."""
    int_list = []
    for i in range(num):
        value = random.randint(0, limit)
        int_list.append(value)
    return int_list

def find_max(random_list):
    max_value = 0
    for i in random_list:
        if i > max_value:
            max_value = i
    return max_value
    
new_list = create_list(100,1000)
print(find_max(new_list))
