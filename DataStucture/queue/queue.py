def enqueue(data,a,rear,Max):

    if(len(a) == Max):
        print("Enough data")
        return
    else:
        a.append(data)
        rear = rear +1

    return a,rear

def dequeue(a):
    if(len(a) < 0):
        print("Empty data")

    else:
        print(a[0])
        del a[0]
        print(a)
    return a

Max = 3
a = []
rear = -1

while(True):

    print("Select 1 (enqueue)or 2(dequeue) (else end)")
    in_data = input()
    in_data = int(in_data)

    if(in_data == 1):
        print("Enter the data")
        data = input()
        data = int(data)
        enqueue(data,a,rear,Max)
        print(a)

    elif(in_data == 2):
        dequeue(a)