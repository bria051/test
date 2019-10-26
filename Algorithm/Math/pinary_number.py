a = int(input())
j_list = [1,1]
for x in range(91):
    j_list.append(j_list[x]+j_list[x+1])
print(j_list[a-1])