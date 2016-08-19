# What is the longest word in Alice in Wonderland?
# How many characters does it have?

f = open('Alice in wonderland.txt', 'r')
longest_word = ''
length = 0

for line in f:
    for word in line.split():
        
        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '')
        word = word.replace('-', '').replace('?', '').replace('!', '')
        word = word.replace('(', '').replace(')', '').replace(':', '')
        word = word.replace('.', '').replace("'", "").replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()
        if len(word) > len(longest_word):
            longest_word = word

print('The longest word in Alice in Wonderland is {}, '
       'and it has {} characters'.format(longest_word, len(longest_word)))

f.close()
