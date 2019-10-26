a = input()
def alphabet(num):
    list = ['a', 'e', 'i', 'o', 'u']
    zero = 0

    for w in range(len(num)):
        for x in range(len(list)):
            if (a[w] == list[x]):
                zero = zero + 1

    return zero


end = alphabet(a)

print(end)