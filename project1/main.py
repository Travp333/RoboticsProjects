colors = [['red', 'green', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']

p = [[1/20, 1/20, 1/20, 1/20, 1/20],
     [1/20, 1/20, 1/20, 1/20, 1/20],
     [1/20, 1/20, 1/20, 1/20, 1/20],
     [1/20, 1/20, 1/20, 1/20, 1/20]]

# Motion encoding
# [0,0] - no move
# [0,1] - move right
# [0,-1] - move left
# [1,0] - move down
# [-1,0] - move up

motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8


def show(p):
    for i in range(len(p)):
        print(p[i])


# Do not delete this comment!
# Do not use any import statements.
# Adding or changing any code above may
# cause the assignment to be graded incorrectly.

# Enter your code here:

pExact = p_move
pUndershoot = 1 - pExact
pHit = sensor_right
pMiss = 1-pHit


def move(p, U): # takes the table of probabilities (p) and one entry of the motions table, that being a list. [0,1], for example (U)
    if (U == 0): # if motion is zero, no change to probability needs to occur
        return p # return same p
    q = [] # create a list
    for i in range(len(p)): # loops through a row of probabilities
        r=[] # create another list
        for j in range(len(p[0])): #loops through individual entries in the row. p[0] since theyre all the same size
            r.append(p[(i - U[0]) % len(p)][(j - U[1]) % len(p[0])] * pExact+
                     p[((i - U[0]) + 1) % len(p)][((j - U[1]) + 1) % len(p[0])] * pUndershoot)
            #adds updated probability to list r after runnning through the formula
        q.append(r) # adds whole list of r to q, recreating the 2d grid
    return q

def sense(p, Z):

    q = []
    for i in range(len(p)):
        r = []
        for j in range(len(p[i])):
            hit = (Z == colors[i][j])
            r.append(p[i][j] * (hit * pHit + (1-hit) * pMiss))
        q.append(r)
    s2 = 0
    for i in range(len(q)):
        s = sum(q[i])
        s2 = s2 + s
        print ("b",s2)

    for i in range(len(q)):
        for j in range(len(q[0])):
            q[i][j] = q[i][j] / s2
    return q

# Your probability array must be printed
# with the following code.

show(p)

for i in range(len(motions)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])

show(p)