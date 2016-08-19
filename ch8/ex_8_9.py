# Write a function that counts how many times a substring occurs in a string.

def count(substr,theStr):
    c = 0
    for i in range(len(theStr)):
        if substr in (theStr[i:(i + len(substr))]):
            c = c + 1
    return c

substring = 'aaa'
string = 'aaaaaa'

print(count(substring, string))
