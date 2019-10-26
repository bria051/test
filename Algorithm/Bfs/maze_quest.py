import collections
queue = collections.deque()

y,x = map(int,input().split())

matrix = []
visited = []
for i in range(y):
    c = input()
    matrix.append([])
    visited.append([])
    for j in range(x):
        matrix[i].append(int(c[j]))
        visited[i].append(1)

queue.append((0, 0, 0))
visited[0][0] = 0

          #우       하       좌        상
arrow = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = 1
while(len(queue) != 0):
    c_y, c_x, count = queue.popleft()

    if(c_x == x-1 and c_y == y-1):
        print(count+1)
        break
    for i in range(len(arrow)):

        t_y, t_x = arrow[i]
        temp_y = c_y + t_y
        temp_x = c_x + t_x

        if(temp_y < y and temp_y >= 0 and temp_x < x and temp_x >= 0):
            if(matrix[temp_y][temp_x] == 1 and visited[temp_y][temp_x] == 1):
                visited[temp_y][temp_x] = 0
                queue.append((temp_y, temp_x, count+1))