# this program allows the user to enter a string. It then prints a table
# of the letters of the alphabet in alphabetical order which occur in the
# string together with the number of times each letter occurs. Case is 
# ignored.

def count_all(the_string):
    letter_count = {}
    the_string = the_string.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in the_string:
        if i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] += 1
    
    for c in alpha:
        print(c, letter_count.get(c, 0))

count_all(input("Please enter a sentence: "))
