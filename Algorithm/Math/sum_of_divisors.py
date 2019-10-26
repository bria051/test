list = []
while(True):
    a = int(input())
    if(a != -1):
        list.append(a)
    else:
        break

list_3 = []
for x in range(len(list)):
    list_2 = []
    num = 0
    for y in range(1,list[x]):

        if(list[x] % y == 0 and list[x] != y):
            list_2.append(y)
            num = num + y
    list_2 = str(list_2)
    list_2 = list_2.replace('[', '')
    list_2 = list_2.replace(']', '')
    list_2 = list_2.replace(',', ' +')

    if(list[x] == num and list[x] != 0):
        list_3.append('%d = %s'%(list[x],list_2))
    else:
        list_3.append('%d is NOT perfect.'%(list[x]))

for x in list_3:
    print(x)