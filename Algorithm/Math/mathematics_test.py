list = []
a,b = map(int,input().split())
for x in range(1,47):
    for y in range(x):
        list.append(x)
num = 0
if(a < b):
    for i in range(b-a+1):
        num = num + list[a-1 + i]
if(a == b):
    num = list[a-1]
print(num)