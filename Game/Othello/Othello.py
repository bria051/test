def make_board(a):
    board = []
    for x in range(a):
        board.append([])
        for y in range(a):
            board[x].append("*")

    num = int(len(board)/2-1)
    board[num][num] = "O"
    board[num][num+1] = "X"
    board[num+1][num] = "X"
    board[num+1][num+1] = "O"

    return board
def print_board(list):
    sentence = ""
    for x in range(len(list)):
        for y in range(len(list[x])):
            sentence += list[x][y]
            if(y != len(list[x])-1):
                sentence += " "
        if(x != len(list)-1):
            sentence += "\n"
    print(sentence)

def width_change(board, mark, num):
    for x in range(len(board[num])):
        if(board[num][x] != '*' and board[num][x] != mark):
            board[num][x] = mark
def height_change(board, mark, num):
    for x in range(len(board[num])):
        if(board[x][num] != '*' and board[x][num] != mark):
            board[x][num] = mark

def width(board):
    for x in range(len(board)):
        num = 0
        front = 0
        back = 1
        blank = ['*', '*']
        while num <= len(board)-1:
            if(front != back):
                if(blank[0] == '*'):
                    if(board[x][num] == 'O'):
                        blank[0] = 'O'
                        front = num
                    elif (board[x][num] == 'X'):
                        blank[0] = 'X'
                        front = num
                if(blank[1] == '*'):
                    if(board[x][3-num] == 'O'):
                        blank[1] = 'O'
                        back = 3-num
                    elif(board[x][3-num] == 'X'):
                        blank[1] = 'X'
                        back = 3-num
            num += 1
        if(blank[0] != '*' and blank[0] == blank[1]):
            width_change(board, blank[0], x)
            return board
def height(board):
    for x in range(len(board[0])):
        num = 0
        front = 0
        back = 1
        blank = ['*', '*']
        while num <= len(board[0])-1:
            if (front != back):
                if(blank[0] == '*'):
                    if(board[num][x] == 'O'):
                        blank[0] = 'O'
                    elif (board[num][x] == 'X'):
                        blank[0] = 'X'
                if(blank[1] == '*'):
                    if(board[3-num][x] == 'O'):
                        blank[1] = 'O'
                    elif(board[3-num][x] == 'X'):
                        blank[1] = 'X'
            num += 1
        if(blank[0] != '*' and blank[0] == blank[1]):
            height_change(board, blank[0], x)
            return board

