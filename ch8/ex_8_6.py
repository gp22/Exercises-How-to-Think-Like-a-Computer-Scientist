# Write a function that reverses its string argument.

def reverseString(string):
    newString = ''
    for i in range(len(string)-1, -1, -1):
        newString = newString + string[i]
    return newString

def mirrorString(string):
    return string + reverseString(string)

print(mirrorString('Jake'))
