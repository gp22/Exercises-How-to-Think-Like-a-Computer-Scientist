# Assign to a variable in your program a triple-quoted string that
# contains your favorite paragraph of text - perhaps a poem, a speech,
# instructions to bake a cake, some inspirational verses, etc.

# Write a function that counts the number of alphabetic characters
# (a through z, or A through Z) in your text and then keeps track of
# how many are the letter ‘e’. 

def count(p):
    c = 0
    charE = 0
    for char in p:
        c = c + 1
        if char == 'e':
            charE = charE + 1
    print('Your text contains', c, 'alphabetic characters, '
          'of which', charE, '(', round(c/charE, 2), '%) are \'e\'.')
    
quote = 'Be content with what you have:\n' \
        'rejoice in the way things are.\n' \
        'When you realize there is nothing lacking,\n' \
        'the whole world belongs to you.\n' \
        '~Lao Tzu'

count(quote)
