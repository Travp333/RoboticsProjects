# write code that moves 1000 times and then prints the
# resulting probability distribution.

p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def move(p, U):
    if (U == 0):
        return p
    q = []
    for i in range(len(p)):
        q.append(p[(i - U - 1) % len(p)] * pOvershoot +
                 p[(i - U) % len(p)] * pExact +
                 p[(i - U + 1) % len(p)] * pUndershoot)
    return q


print (p)

i = 1
while i <= 1000:
    p = move(p,1)
    i += 1

print(move(p,1))