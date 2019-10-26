input_len = int(input())
alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word_list = []

for x in range(input_len):
    b = input()
    word_list.append(b)

word_list = list(set(word_list))

for x in range(len(word_list)):
    for y in range(len(word_list)-1):
        if(len(word_list[y]) > len(word_list[y+1])):
            word_list[y],word_list[y+1] = word_list[y+1],word_list[y]

list_2 = []
blank = ''
for x in range(len(word_list)):
    blank = word_list[x]
    list = []
    for y in range(len(blank)):
        list.append(blank[y])
    for y in range(len(list)):
        for z in range(len(alpa)):
            if(list[y] == alpa[z]):
                list[y] = z
    list_2.append(list)


for x in range(len(list_2)-1):
    for y in range(len(list_2[x])):
        if(list_2[x][y] > list_2[x+1][y] and len(list_2[x]) == len(list_2[x+1])):
            list_2[x][y],list_2[x+1][y] = list_2[x+1][y],list_2[x][y]
            word_list[x],word_list[x+1] = word_list[x+1],word_list[x]

for x in range(len(word_list)):
    print(word_list[x])
    "fail"