# Write a program called alice_words.py that creates a text file
# named alice_words.txt containing an alphabetical listing of all
# the words, and the number of times each occurs, in the text version
# of Alice’s Adventures in Wonderland. (You can obtain a free plain
# text version of the book, along with many others, from
# http://www.gutenberg.org.)

def count_words(infile, outfile):
    word_count = {}
    key_list = []
    alice = open(infile, 'r')
    alice_words = open(outfile, 'w')
    line = alice.readline()

    while line:
        line = line.lower()
        line = line.split(' ')
        line = only_alpha(line)
        for word in line:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        line = alice.readline()

    for key in word_count:
        key_list += [key]

    key_list.sort()
    right_margin = len(max(key_list, key=len)) + 2
    
    for key in key_list:
        margin_offset = right_margin - len(key)
        newline = str(key) + ('-' * margin_offset) + str(word_count[key])
        alice_words.write(newline + '\n')
        
    alice.close()
    alice_words.close()
    
def only_alpha(the_list):
    """ returns a copy of the_list with all non-alpha characters \
        removed, except for ' """
    
    accepted = 'abcdefghijklmnopqrstuvwxyz\''
    new_list = []
    for word in the_list:
        new_word = ''
        for char in word:
            if char in accepted:
                new_word += char
        new_list.append(new_word)
    return new_list

count_words('Alice in wonderland.txt', 'alice_words.txt')
