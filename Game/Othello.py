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

board = make_board(4)

def print_board(list):
    for x in range(len(list)):
        print(list[x])

print_board(board)

#first begining will be the O
for x in range(len(board)):
    for y in range(len(board[x])):
        if(board[x][y] == "X"):
            board #<-- change plz