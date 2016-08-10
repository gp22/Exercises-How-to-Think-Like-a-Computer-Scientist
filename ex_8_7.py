# Write a function that removes all occurrences of a given letter from a string.

def removeChar(string, char):
    newStr = ''
    for c in string:
        if c != char:
            newStr = newStr + c
    return newStr

print(removeChar('Write a function that removes all occurrences of a given letter from a string.', 'e'))
