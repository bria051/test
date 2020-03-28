a = input()

box = []
for x in range(len(a)):
    box.append(a[x])

front = ['[', '{', '(']
back = [']', '}', ')']

def s_output(list):
    a = list[len(list)-1]
    del list[len(list)-1]

    return a

pocket = []
num = 0
flag = 0
while True:

    if num > len(box)-1 and len(pocket) == 0:
        print("symmetry")
        break
    elif num > len(box)-1 and len(pocket) != 0:
        print("none")
        break

    for x in range(len(front)):
        if box[num] == front[x]:
            pocket.append(back[x])
            flag = 1
            break

    if flag != 1:
        for x in range(len(pocket)):
            if box[num] == pocket[len(pocket)-1]:
                s_output(pocket)
                flag = 1
                break
        if flag != 1:
            print("none")
            break

    flag = 0
    num += 1