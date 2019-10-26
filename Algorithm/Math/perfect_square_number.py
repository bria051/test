a = int(input())
b = int(input())


num = 1
list = []
while(True):
    if(num * num <= b):
        if(num * num >= a):
            list.append(num * num)
            num += 1
        else:
            num += 1
    else:
        break

total = 0
for x in range(len(list)):
    total = list[x] + total

if(total == 0):
    print(-1)
else:
    print(total)
    print(list[0])