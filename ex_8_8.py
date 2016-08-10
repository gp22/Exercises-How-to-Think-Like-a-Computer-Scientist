# Write a function that recognizes palindromes.
# (Hint: use your reverse function to make this easy!).

def isPalindrome(string):
    if len(string) % 2 == 0:
        half = halfStr(string)
        palindromeTest = mirrorString(half)
    else:
        half = halfStr(string)
        middleChar = string[len(string) // 2]
        palindromeTest = half + middleChar + reverseString(half)
        
    return string == palindromeTest
    
def halfStr(string):
    halfStr = string[:len(string) // 2]
    return halfStr

def reverseString(string):
    newString = ''
    for i in range(len(string)-1, -1, -1):
        newString = newString + string[i]
    return newString

def mirrorString(string):
    return string + reverseString(string)

print(isPalindrome('babacccabab'))

