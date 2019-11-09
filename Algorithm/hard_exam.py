def solution(s):
    answer = []
    temp = s.split('{')

    list = []
    for temp_list in temp:
        if(len(temp_list) == 0):
            continue
        else:
            values = temp_list.split('}')[0]
            list.append(values.split(','))

    for x in range(len(list)):
        for y in range(len(list[x])):
            list[x][y] = int(list[x][y])
    print(list)

    for w in range(len(list)):
        for x in range(len(list)-1):
            if(len(list[x]) > len(list[x+1])):
               list[x], list[x+1] = list[x+1], list[x]
    print(list)

    answer = []
    for temp in list:
        if(len(temp) == 1):
            answer.append(temp[0])
        else:
            flag = 0
            for k in temp:
                if k not in answer:
                    answer.append(k)
                    break

    return answer

print(solution("{{3,2,1},{1,2},{1,2,4,3},{1}}"))

