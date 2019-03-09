l = []

for i in range(8):

    l.append(int(input()))

b = [1,2,3,4,5,6,7,8]



for i in range(len(l)):
    for x in range(len(l)-1):

        if(l[x] < l[x + 1]):
            l[x],l[x+1] = l[x+1],l[x]
            b[x],b[x+1] = b[x+1],b[x]

for i in range(5):
    for x in range(5 - 1):
        if(b[x] > b[x+1]):
            b[x],b[x+1] = b[x+1],b[x]

print(l[0]+l[1]+l[2]+l[3]+l[4])

print("%d %d %d %d %d"%(b[0],b[1],b[2],b[3],b[4]))

#--------------------------------------------------

input_len = int(input())
number_list = input()
number_list = number_list.split(' ')

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

for x in range(len(number_list)):
    for y in range(len(number_list) - 1):
        if (number_list[y] > number_list[y+1]):
            number_list[y],number_list[y+1] = number_list[y+1],number_list[y]
zero = 0
for x in range(len(number_list)):
    n = number_list[x] * (number_list - x)
    zero = zero + n
print(zero)
