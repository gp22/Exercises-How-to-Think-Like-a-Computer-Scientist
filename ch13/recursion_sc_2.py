def removeWhite(s):
    s = s.replace(' ', '')
    s = s.replace("'", '')
    return s

def isPal(s):
    if removeWhite(s) == reverse(removeWhite(s)):
        return True
    else:
        return False

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

print(isPal("radar"))
