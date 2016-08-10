# Write a function that reverses its string argument.

def reverseString(string):
    newString = ''
    for i in range(len(string)-1, -1, -1):
        newString = newString + string[i]
    return newString

print(reverseString('Reverse this string'))
