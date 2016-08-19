# Print out a neatly formatted multiplication table, up to 12 x 12

def multiplyTable(x, y):
    for i in range(1, y+1):
        print(x, ' * ', str(i).rjust(len(str(y))), ' = ', x * i)

multiplyTable(12, 12)
