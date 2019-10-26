a = input()
number_list = []

for i in range(len(a)):
    number_list.append(a[i])


n2 = ['A','B','C']
n3 = ['D','E','F']
n4 = ['G','H','I']
n5 = ['J','K','L']
n6 = ['M','N','O']
n7 = ['P','Q','R','S']
n8 = ['T','U','V']
n9 = ['W','X','Y','Z']

numbers = [n2,n3,n4,n5,n6,n7,n8,n9]

for w in range(len(numbers)):
    for x in range(len(number_list)):
        for y in range(len(numbers[w])):
            if(number_list[x] == numbers[w][y]):
                number_list[x] = w + 3

zero = 0
for z in range(len(number_list)):
    zero = zero + number_list[z]
print(zero)