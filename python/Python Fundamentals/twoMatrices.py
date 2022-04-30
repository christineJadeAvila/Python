# multiply two matrices using nested loops

# 3x3 matrix
x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# 3x4 matrix
y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

# Result is 3 x 4 
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

#iterate through rows of x
for rows in range(len(x)):
    #iterate through columns of y
    for cols in range(len(y[0])):
        # iterate through rows of y
        for row in range(len(y)):
            result[rows][cols] += x[rows][row] * y[row][cols]

for results in result: 
    print(results)

    
