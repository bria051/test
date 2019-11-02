'''
for x in range(1,101):
    if(x % 10 == 3 or x % 10 == 6 or x % 10 == 9):
        print(x)

#----------------------------------------------------------------------------------

n = 0
for x in range(1,11):
    n = n + x
print(n)

#----------------------------------------------------------------------------------

for i in range(1,10):
    for j in range(1,10):
        print("%d x %d = %d"%(i,j,i*j))

#----------------------------------------------------------------------------------

a = input()
a = int(a)
for x in range(1,10):
    print("%d x %d = %d"%(a,x,a*x))

#----------------------------------------------------------------------------------

while(True):
    a = input()
    a = int(a)
    if(a==0):
        break
    for x in range(1,10):
        print("%d x %d = %d"%(a,x,a*x))

#----------------------------------------------------------------------------------

while(True):
    print("첫번째 숫자를 입력하세요 : ")
    a = input()
    a = int(a)
    print("두번째 숫자를 입력하세요 : ")
    b = input()
    b = int(b)
    print("부호를 정하세요 (1번은 더하기 , 2번은 빼기, 3번은 곱하기, 4번은 나누기) : ")
    c = input()

    if(c == '+'):
        print("%d + %d = %d"%(a,b,a+b))
    elif(c == '-'):
        print("%d - %d = %d"%(a,b,a-b))
    elif(c == 'x'):
        print("%d x %d = %d" % (a,b,a*b))
    elif(c == '/'):
        print("%d / %d = %d" % (a,b,a/b))


#----------------------------------------------------------------------------------

import random

a = []
for x in range(10):
    a.append(random.randrange(1,101))

print(a)

#----------------------------------------------------------------------------------

import random

a = []
n = 0
for x in range(10):
    a.append(random.randrange(1,10))

    n = n + a[x]

print(n)

#----------------------------------------------------------------------------------

import random
a = []
i = 0

for x in range(10):
    a.append(random.randrange(1,10))

    if(a[x] > i):
        i = a[x]
print(i)

#----------------------------------------------------------------------------------

import random
a = []
i = 10

for x in range(10):
    a.append(random.randrange(1,10))

    if(a[x] < i):
        i = a[x]
print(i)

#----------------------------------------------------------------------------------

import random

a = []

for x in range(100):
    a.append(random.randrange(1,101))
print(a)

for x in range(len(a)):
    print(a[x])

'''
