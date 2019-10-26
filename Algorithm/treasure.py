a = int(input())
b = input()
b = b.split(' ')
c = input()
c = c.split(' ')

for i in range(len(b)):
    b[i] = int(b[i])
for i in range(len(c)):
    c[i] = int(c[i])

for x in range(len(b)):
    for y in range(len(b)-1):
        if(b[y] > b[y + 1]):
            b[y],b[y + 1] = b[y + 1],b[y]

for x in range(len(b)):
    for y in range(len(b)-1):
        if(c[y] < c[y + 1]):
            c[y],c[y + 1] = c[y + 1],c[y]

zero = 0

for x in range(len(b)):
    zero = zero + (b[x] * c[x])
print(zero)