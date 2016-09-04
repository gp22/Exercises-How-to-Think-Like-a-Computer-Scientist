# Create a list containing 100 random integers between 0 and 1000
# (use iteration, append, and the random module). Write a function
# called average that will take the list as a parameter and return
# the average.

import random

def create_list(num, limit):
    """create a list containing num random integers from 0 to limit."""
    int_list = []
    for i in range(num):
        value = random.randint(0, limit)
        int_list.append(value)
    return int_list

def average(averaged_list):
    sum = 0
    for i in averaged_list:
        sum = sum + i
    average = sum / len(averaged_list)
    return average
    
new_list = create_list(100,1000)
print(average(new_list))
