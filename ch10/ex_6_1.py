# Using the text file studentdata.txt write a program that prints out
# the names of students that have more than six quiz scores.

data = open('studentdata.txt', 'r')
line = data.readline()
line = line.split()

while line:
    if len(line) > 6:
        print(line[0])
    line = data.readline()
    line = line.split()

data.close()
