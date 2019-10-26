a = input()
list = []
list_2 = []
ce = ['C','A','M','B','R','I','D','G','E']

for i in range(len(a)):
    list.append(a[i])

for x in range(len(list)):
    for y in range(len(ce)):
        if(list[x] == ce[y]):
            list[x] = 0
for x in range(len(list)):
    if(list[x] != 0):
        list_2.append(list[x])

list_2 = ''.join(list_2)

print(list_2)