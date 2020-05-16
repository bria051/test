infix = input('중위식 입력: ').split()
postfix = []
stack = []
priority = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

for x in infix:
    if x.isdigit():
        postfix.append(x)
    else:
        if len(stack) == 0:
            stack.append(x)
        elif priority[stack[-1]] > priority[x]:
            postfix.append(stack.pop())
            stack.append(x)
        else:
            stack.append(x)

while len(stack) != 0:
    postfix.append(stack.pop())

print('후위식:', postfix)

for x in postfix:
    if x.isdigit():
        stack.append(x)
    else:
        if x == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif x == '-':
            stack.append(int(stack.pop()) - int(stack.pop()))
        elif x == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif x == '/':
            stack.append(int(stack.pop()) / int(stack.pop()))
print(stack.pop())