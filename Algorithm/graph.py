location = [(3, 3), (4, 4), (2, 2)]
answer = [(2, 3), (3, 4), (4, 5)]

num_list = []
for i in range(len(answer)):
    num_list.append(0)

count1 = 0
for a, b in answer:
    for x, y in location:
        if count1 >= len(answer):
            count1 = count1 % len(answer)
        num_list[count1] += (abs(a-x) + abs(b-y))
        count1 += 1
    count1 += 2

num = num_list[0]
for i in num_list:
    if num > i:
        num = i
print(num)


#============================================


location = [[3, 3], [4, 4], [2, 2]]
answer = [[2, 3], [3, 4], [4, 5]]

box = len(location)
num_list = []
for i in range(len(answer)):
    num_list.append(0)

for x in range(box):
    for y in range(box):
        num_list[x] += abs((answer[y][0] + answer[y][1]) - (location[y][0] + location[y][1]))
    location = location[box-1:] + location[:box-1]

num = num_list[0]
for i in num_list:
    if num > i:
        num = i
print(num)