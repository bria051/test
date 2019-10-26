a = input()

list =[]
for x in range(len(a)):
    list.append(a[x])

number_case = ['0','1','2','3','4','5','7','8']

blank = 0
blank_2 = 0
blank_3 = 0
for x in number_case:
    blank_2 = 0
    blank_3 = 0
    for y in range(len(list)):
        if(list[y] == '6' or list[y] == '9'):
            blank_3 += 1
        elif(list[y] == x):
            blank_2 += 1
    blank_3 = int((blank_3-(blank_3%2))/2+blank_3%2)

    if (blank_2 > blank_3):
        if (blank < blank_2):
            blank = blank_2
    else:
        if (blank < blank_3):
            blank = blank_3
print(blank)