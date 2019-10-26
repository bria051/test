list = []
a = input()


for x in range(len(a)):
    list.append(a[x])
    list[x] = int(list[x])


for j in range(len(list)):
    for i in range(len(list)-1):
        if(list[i] < list[i+1]):
            list[i],list[i+1] = list[i+1],list[i]

for x in range(len(a)):
    list[x] = str(list[x])

num = ''.join(list)
num = int(num)

if(num % 30 == 0 and num > 0):
    print(num)
elif(num % 30 != 0 or num <= 0):
    print(-1)
    "fail"