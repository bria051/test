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
    n = number_list[x] * (input_len - x)
    zero = zero + n
print(zero)