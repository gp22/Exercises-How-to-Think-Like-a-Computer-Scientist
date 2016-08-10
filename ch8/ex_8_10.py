# Write a function that removes the first occurrence of a string from
# another string.

def remove(substr,theStr):
    if substr in theStr:
        loc = theStr.find(substr)   # find the beginning of substr
        subLen = len(substr)        # find the length of substr
        return theStr[:loc] + theStr[subLen + loc:]

    else: return theStr


print(remove('egg', 'bicycle'))
