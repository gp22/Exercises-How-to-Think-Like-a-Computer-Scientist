# Write a function called remove_dups that takes a string and creates
# a new string by only adding those characters that are not already
# present. In other words, there will never be a duplicate letter
# added to the new string.

def remove_dups(astring):
    newStr = ''
    for c in astring:
        if newStr.count(c) < 1:
            newStr = newStr + c

    return newStr
        
print(remove_dups("mississippi"))   #should print misp
