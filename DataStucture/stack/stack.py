def push(sta,rear):

    if (len(sta) == max):
        print("초과")
        return

    num = input()
    num = int(num)
    sta.append(num)
    rear = rear + 1

    return rear

def pop(rear,sta):
    print(rear)
    if (rear < 0):
        print("미만")
        return

    print(sta.pop(rear))

    rear = rear -1

    return rear

sta = []
max = 5
rear = -1

while(True):

    val = input()
    val = int(val)

    if(val == 1):
        rear = push(sta,rear)
        print(sta)
    elif(val == 2):
        rear = pop(rear,sta)
