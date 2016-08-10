# Write a function that removes all occurrences of a string from another string.

def remove_all(substr,theStr):
    if substr not in theStr: return theStr
    
    newStr = theStr
    while substr in newStr:
        loc = newStr.find(substr)   # find the beginning of substr
        subLen = len(substr)        # find the length of substr
        newStr = newStr[:loc] + newStr[subLen + loc:]

    return newStr

print(remove_all('a ', 'banana banana '))
