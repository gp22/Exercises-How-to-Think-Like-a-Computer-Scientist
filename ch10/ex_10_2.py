# Using the text file studentdata.txt (shown in exercise 1) write a
# program that calculates the average grade for each student, and print
# out the student’s name along with their average grade.

data = open('studentdata.txt', 'r')
line = data.readline()
line = line.split()

while line:
    print(line[0], 'average score: ', end='')
    total = 0
    for i in range(1, len(line)):
        index_value = int(line[i])
        total = total + index_value
    average = total / (len(line)-1)
    print(average)
    line = data.readline()
    line = line.split()

data.close()
