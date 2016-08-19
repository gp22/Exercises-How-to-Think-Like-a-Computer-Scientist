# Using the text file studentdata.txt (shown in exercise 1) write a
# program that calculates the minimum and maximum score for each student.
# Print out their name as well.

data = open('studentdata.txt', 'r')
line = data.readline()
line = line.split()

while line:
    score_list = [int(i) for i in line[1:]]
    max_score = max(score_list)
    min_score = min(score_list)
    print(line[0], 'max score:', max_score, 'min score:', min_score)                    
    line = data.readline()
    line = line.split()

data.close()
