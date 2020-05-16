import tkinter as tk

# 폰트
FONT = ('맑은 고딕', 20)

# 창 생성 및 설정(메인)
window = tk.Tk()
window.title('계산기')
window.geometry("380x330")
window.resizable(False, False)

# 텍스트 입력 위젯 생성
textbox = tk.Entry(window, font=FONT)
textbox.configure(bd=0)
textbox.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# 버튼 위젯 생성(숫자)
numpad7 = tk.Button(window, font=FONT, text='7', width=4, command=lambda: textbox.insert('end', '7'))
numpad7.grid(row=1, column=0)
numpad8 = tk.Button(window, font=FONT, text='8', width=4, command=lambda: textbox.insert('end', '8'))
numpad8.grid(row=1, column=1)
numpad9 = tk.Button(window, font=FONT, text='9', width=4, command=lambda: textbox.insert('end', '9'))
numpad9.grid(row=1, column=2)
numpad4 = tk.Button(window, font=FONT, text='4', width=4, command=lambda: textbox.insert('end', '4'))
numpad4.grid(row=2, column=0)
numpad5 = tk.Button(window, font=FONT, text='5', width=4, command=lambda: textbox.insert('end', '5'))
numpad5.grid(row=2, column=1)
numpad6 = tk.Button(window, font=FONT, text='6', width=4, command=lambda: textbox.insert('end', '6'))
numpad6.grid(row=2, column=2)
numpad1 = tk.Button(window, font=FONT, text='1', width=4, command=lambda: textbox.insert('end', '1'))
numpad1.grid(row=3, column=0)
numpad2 = tk.Button(window, font=FONT, text='2', width=4, command=lambda: textbox.insert('end', '2'))
numpad2.grid(row=3, column=1)
numpad3 = tk.Button(window, font=FONT, text='3', width=4, command=lambda: textbox.insert('end', '3'))
numpad3.grid(row=3, column=2)
numpad0 = tk.Button(window, font=FONT, text=0, width=4, command=lambda: textbox.insert('end', '0'))
numpad0.grid(row=4, column=1)

def split_all(infix):
    separate = []
    for x in infix:
        if x.isdigit():
            if len(separate) == 0 or not(separate[-1].isdigit()):
                separate.append(x)
            else:
                separate.append(separate.pop() + x)
        else:
            if x != ' ':
                separate.append(x)
    return separate

# TODO: 입력받은 infix를 postfix로 변환하고 계산할 것
def operate(string):
    infix = split_all(string)     # textbox로 부터 infix 문자열 받기
    postfix = []
    # postfix로 변환후 계산
    stack = []
    priority = {'+': 0, '-': 0, '*': 1, '/': 1}
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

    for x in postfix:
        if x.isdigit():
            stack.append(x)
        else:
            beta = int(stack.pop())
            alpha = int(stack.pop())
            if x == '+':
                stack.append(alpha + beta)
            elif x == '-':
                stack.append(alpha - beta)
            elif x == '*':
                stack.append(alpha * beta)
            elif x == '/':
                stack.append(alpha / beta)

    textbox.delete(0, 'end')
    textbox.insert('end', stack.pop())

# 버튼 위젯 생성(=)
enter = tk.Button(window, font=FONT, text='=', width=4, command=lambda: operate(textbox.get()))
enter.grid(row=4, column=2)

# 버튼 위젯 생성(연산자+-*/)
plus = tk.Button(window, font=FONT, text='+', width=4, command=lambda: textbox.insert('end', '+'))
plus.grid(row=1, column=3)
minus = tk.Button(window, font=FONT, text='-', width=4, command=lambda: textbox.insert('end', '-'))
minus.grid(row=2, column=3)
mul = tk.Button(window, font=FONT, text='*', width=4, command=lambda: textbox.insert('end', '*'))
mul.grid(row=3, column=3)
div = tk.Button(window, font=FONT, text='/', width=4, command=lambda: textbox.insert('end', '/'))
div.grid(row=4, column=3)

# 버튼 위젯 생성(Clear)
clear = tk.Button(window, font=FONT, text='C', width=4, command=lambda: textbox.delete(0, 'end'))
clear.grid(row=4, column=0)

# 이벤트 루프 실행
window.mainloop()
