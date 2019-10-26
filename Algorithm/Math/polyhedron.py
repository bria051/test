input_len = int(input())

number_list = []

ent = []

for x in range((input_len)):
    b,c = map(int,input().split(' '))


    number_list.append([b,c])

    ent.append(c - b + 2)

for x in range(len(ent)):
    print(ent[x])