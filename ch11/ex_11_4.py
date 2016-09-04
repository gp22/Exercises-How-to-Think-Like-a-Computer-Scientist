# Write a program that asks the user for a sentence in English
# and then translates that sentence to Pirate.

# create the pirate dictionary
english2pirate = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie',
                  'boy': 'matey', 'madam': 'proud beauty',
                  'professor': 'foul blaggart', 'restaurant': 'galley',
                  'your': 'yer', 'excuse': 'arr', 'students': 'swabbies',
                  'are': 'be', 'lawyer': 'foul blaggart', 'the': "th'",
                  'restroom': 'head', 'my': 'me', 'hello': 'avast', 'is': 'be',
                  'man': 'matey'}

user_input = input('Enter a sentence > ')
for word in user_input.split():
    if word in english2pirate:
        print(english2pirate[word])
    else:
        print(word)

