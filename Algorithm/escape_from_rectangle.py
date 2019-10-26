a,b,c,d = map(int,input().split())
list = [a,b,c-a,d-b]

num = 1000
for x in range(4):
    if(list[x] < num):
        num = list[x]
print(num)