a = int(input())
matrix = []
for i in range(a+1):
    matrix.append(0)
matrix[0] = 0
matrix[1] = 1

for i in range(2, a+1):
    matrix[i] = matrix[i-1] + matrix[i-2]

print(matrix[a])
"fail"