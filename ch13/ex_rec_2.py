# A recursive function to reverse a list.

def reverseList(lst):
    if len(lst) == 1:
        return lst
    else:
        index = lst[0]
        del lst[0]
        reverseList(lst)
        lst.append(index)

myList = [1,2,3,4,5]
reverseList(myList)
print(myList)
