# Program to multiply two matrices using nested loops

import random                     #This is the line that takes up most of the time (3.215s)

N = 250

# NxN matrix
X = []
for i in range(N):                #Randrange and randint are the functions called for more times (125250)
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:                 #Here it is printing the resulting matrices, 250 of them; maybe it is not very useful...?
    print(r)
