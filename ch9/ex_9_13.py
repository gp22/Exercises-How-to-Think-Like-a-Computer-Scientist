# Write a function replace(s, old, new) that replaces all occurences
# of old with new in a string s.

def replace(s, old, new):
    newstring = ''
    for char in s:
        if char == old:
            newstring = newstring + new
        else:
            newstring = newstring + char
    return newstring
            
print(replace('Bookkeeper','e','A'))

