# Although Python provides us with many list methods, it is good
# practice and very instructive to think about how they are implemented.
# Implement a Python function that works like the following: count, in,
# reverse, index, insert

def my_count(the_list, value):
    count = 0
    for index in the_list:
        if index == value:
            count = count + 1
    return count

def in_list(the_list, value):
    for index in the_list:
        if index == value:
            return True
    return False

def reverse_list(the_list):
    newlist = []
    for index in the_list:
        newlist = [index] + newlist
    return newlist

def list_index(the_list, value):
    for i in range(len(the_list)):
        if the_list[i] == value:
            return i
    return -1

def list_insert(index, value, the_list):
    newlist = the_list[:index] + [value] + the_list[index:]
    return newlist

mylist = [1, 3, 4, 5, 3, 6, 8, 'Jake']
print(list_insert(2, 'dog', mylist))
