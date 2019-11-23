a = int(input())

if(a == 1):
    print(1)

else:
    li = []
    while (True):
        if(a/2 == 1):
            li.append(0)
            li.append(1)
            break
        else:
            if(a % 2 == 0):
                li.append(0)
            else:
                li.append(1)
            a //= 2
    st = []
    for x in range(len(li)):
        st.append(li[len(li)-1-x])
    print(st)


b = input()

list = []
for x in range(len(b)):
    list.append(int(b[x]))

none = []
for x in range(len(list)):
    none.append(list[len(list)-1-x])


total = 0
num = 0
while num < len(list):
    if(none[0] == 1):
        total += 1
    else:
        if(none[num] == 1):
            total += 2**num
    num += 1
print(total)