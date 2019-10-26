a = int(input())
list = []
for x in range(a):
    b = int(input())
    list.append(b)

num_list = [1]
for x in range(31):
    num_list.append(int(2*(num_list[x]+0.5)))

for x in range(a):
    print(num_list[(list[x])-1])