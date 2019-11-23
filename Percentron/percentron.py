def And(x1, x2):
    y = 5 * (x1 + x2)
    if(y > 9):
        return 1
    else:
        return 0

def Or(x1, x2):
    y = 5 * (x1 + x2)
    if(y > 4):
        return 1
    else:
        return 0

def Not_And(x1, x2):
    y = 5 * (x1 + x2)
    if(y < 9):
        return 1
    else:
        return 0

And(1,1)
Or(1,1)
Not_And(1,1)



print(And(Or(0,0), Not_And(0,0)))
print(And(Or(1,0), Not_And(1,0)))
print(And(Or(0,1), Not_And(0,1)))
print(And(Or(1,1), Not_And(1,1)))