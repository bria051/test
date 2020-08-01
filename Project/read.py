import time

def read_data():
    f = open("db_file.txt", "r")

    lines = f.readlines()

    box = [[] for i in range(len(lines)-1)]

    for x in range(1, len(lines)):
        sentence = ''

        for y in range(len(lines[x])):
            if lines[x][y] != ',':
                if lines[x][y] != ' ':
                    sentence += lines[x][y]
            else:
                box[x-1].append(sentence)
                sentence = ''
            if y == len(lines[x])-1:
                limcy = sentence.split('\n')
                box[x-1].append(limcy[0])
    f.close()

    return box

def sort():
    box = read_data()

    for x in range(len(box)):
        for y in range(len(box)-1):
            if box[y][2] > box[y+1][2]:
                box[y], box[y + 1] = box[y + 1], box[y]

    return box


# import time
# a = time.strftime('%Y-%m-%d %H:%M:%S')
# print(a)
#
# time.sleep(2)
#
# b = time.strftime('%Y-%m-%d %H:%M:%S')
# print(b)
#
# c = "2020-08-03"
#
# if a > c :
#     print("bye")
# else:
#     print("hi")