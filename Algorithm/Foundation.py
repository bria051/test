
def num(a, b):
    c = a + b
    return c

def num1(a, b):
    c = a - b
    return c

def num2(a, b):
    c = a * b
    return c

def num3(a, b):
    c = a / b
    return c

a = input()
a = int(a)

if (a == 1):
    d = num(10, 5)
    print(d)
if (a == 2):
    d = num1(10, 5)
    print(d)
if (a == 3):
    d = num2(10, 5)
    print(d)
if (a == 4):
    d = num3(10, 5)
    print(d)

#----------------------------------------------------------------------------------

def num(a):
    for x in range(len(a)):
         if(x % 2 == 0):
             print(a[x])

def num2(a):
    for x in range(len(a)):
        if(x % 2 != 0):
            print(a[x])

i = []

for x in range(101):
    i.append(x)

b = input()
b = int(b)

if(b == 1):
    c = num(i)
    print(c)
elif(b == 2):
    c = num2(i)
    print(c)

#----------------------------------------------------------------------------------

def num(a,i):
    for x in range(len(a)):
        if(len(a[x]) < i):
            i = len(a[x])

a = ["Where","When","How"]

i = 100

num(a,i)

#----------------------------------------------------------------------------------

a = []

for x in range(101):
    a.append(0)

for y in range(101):
    for z in range(2,y):
        if(y % z == 0):
            a[y] = 1

for i in range(3,101):
    if(a[i] != 1):
        print(i)

#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------

f = open("test.txt","w")

for i in range(1,10):
    f.write("\n")
    for j in range(1,10):
        f.write(str(i)+"x"+str(j)+"="+str(i*j)+" ")

#----------------------------------------------------------------------------------

f = open("test.txt", "r")
line = f.readlines()
print(line)

#----------------------------------------------------------------------------------

f = open("test.txt", "r")
j = input()
j = int(j)

line = f.readlines()
print(line[j])

#----------------------------------------------------------------------------------

a = [4,2,8,9,6,1,5]
num = 0
for i in range(6):
    for x in range(6):
        if (a[x] > a[x+1]):
            num = a[x]
            a[x] = a[x+1]
            a[x+1] = num
print(a)
#----------------------------------------------------------------------------------


"""

#2018.11.13 gg
a = input()
ai = []

for x in range(len(a)):
    ai.append(0)
for x in range(len(a)):
    ai[int(a[x])] = ai[int(a[x])] +1


b = input()
bi = []

for x in range(len(b)):
    bi.append(0)
for x in range(len(b)):
    bi[int(b[x])] = bi[int(b[x])] +1

for x in range(len(bi)):
    if(ai[x] != bi[x]):
        print("different")
        break
"""
a = input()

for x in range(len(a)):
    if(a[0+x] == a[(len(a)-1)-x]):
        i = 0
    else:
        i = 1

if (i == 0):
    print("ss")
elif(i == 1):
    print("nn")

#-------------------------------------------------------------

def sun(a):
    for x in range(int(len(a) / 2)):
        if (a[x] == a[(len(a) - 1) - x]):
            num = 0
            return num
        else:
            num = 1
            return num
            break

num = 0


while(True):

    a = input()
    num = sun(a)
    if (num == 0):

        print("ss")
    elif (num == 1):

        print("nn")
"""
"""
a = [3,4,2,1,5,9]
num = 0

flag = 0
for w in range(len(a)):
    flag = 0
    for x in range(w,len(a)):
        print('w',w)
        print('num',num)
        if (a[num] > a[x]):
            num = x
            flag = 1
    if(flag == 1):
        a[w],a[num] = a[num],a[w]
    print(a)
"""
"""
a = 0
b = [1,5,4,2]
for w in range(1,len(b)):
    for x in range(len(b)):
        a = b[w]
        print(a)
        if(b[x] > a):
            b[w] = b[x]
            b[x] = a
    print(b)


a = [1,5,2,4]

for x in range(1,len(a)):
    i = a[x]
    j = x
    while(j > 0 and a[j-1] > i):
        a[j] = a[j-1]
        j = j - 1

    a[j] = i
    print(a)
"""
"""
a,b,c,d,e,f,g = map(int,input().split())

list = [a,b,c,d,e,f,g]

s = 0
m = 0
l = 0

for x in range(len(list)):
    if (list[x] < 10):
        s = list[x] + s
    elif (list[x] > 9 and list[x] < 100):
        m = list[x] + m
    elif (list[x] > 99 and list[x] < 1000):
        l = list[x] + l
print("%d %d %d"%(s,m,l))
"""
def coin(num,num1,num2,num3):
    l = 0
    ll = 0
    lll = 0

    if(num/num1 > 0):
        l = (num-(num%num1))/num1
    if((num%num1)/num2 > 0):
        ll = ((num%num1)-((num%num1)%num2))/num2
    if(((num%num1)%num2)/num3 > 0):
        lll = (((num%num1)%num2)-(((num%num1)%num2)%num3))/num3

    return l,ll,lll


c1,c2,c3 = coin(1200,500,100,10)
print(c1+c2+c3)


from math import sqrt

all = {
'us1' : {'mov1':5,'mov2':2,'mov3':3.5},
'us2' : {'mov2':5,'mov3':2},
'us3' : {'mov1':2.5,'mov2':4,'mov3':2},
'us4' : {'mov1':3.5,'mov2':1,'mov3':3}
}

us2_bs = all.get('us2').get('mov3')
us1_bs = all.get('us1').get('mov3')
num = us2_bs - us1_bs
us2_bs = all.get('us2').get('mov2')
us1_bs = all.get('us1').get('mov2')
num_2 = us2_bs - us1_bs

us2_bs = all.get('us2').get('mov3')
us3_bs = all.get('us3').get('mov3')
num_3 = us2_bs - us3_bs
us2_bs = all.get('us2').get('mov2')
us3_bs = all.get('us3').get('mov2')
num_4 = us2_bs - us3_bs

us2_bs = all.get('us2').get('mov3')
us4_bs = all.get('us4').get('mov3')
num_5 = us2_bs - us4_bs
us2_bs = all.get('us2').get('mov2')
us4_bs = all.get('us4').get('mov2')
num_6 = us2_bs - us4_bs

a = "%.5f"%(1/(1 + sqrt((pow(num,2)) + pow(num_2,2))))
b = "%.5f"%(1/(1 + sqrt((pow(num_3,2)) + pow(num_4,2))))
c = "%.5f"%(1/(1 + sqrt((pow(num_5,2)) + pow(num_6,2))))
ls = [a,b,c]

print(ls)

for x in ls:
    if(1 > 1):
        print(5)
    elif(b > x):
        print(2.5)
    elif(c > x):
        print(3.5)

"""

from math import sqrt

def sim(num1,num2):
    return 1/(1 + sqrt((pow(num1,2)) + pow(num2,2)))

for x in all:
    if (x != 'us2'):
        num1 = all.get('us2').get('mov2') - all.get(x).get('mov2')
        num2 = all.get('us2').get('mov3') - all.get(x).get('mov3')
        print(x," : ",sim(num1,num2))

        print(sim(num1, num2))
"""
"""
import cv2

img = cv2.imread('go.jpeg', cv2.IMREAD_COLOR)
height, width, channel = img.shape
print(height, width, channel)


def img_load(img):
    cv2.imshow('temp', img)
    cv2.waitKey(10000)


print('Enter the imag name :')
img_name = input()

print('Enter the numaber')
a = int(input())
flag = 1
M = cv2.getRotationMatrix2D((width / 2, height / 2), 1, 1)

if (flag == 1):
    img = cv2.imread(img_name, cv2.IMREAD_COLOR)

    if (a == 1):
        img = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        img_load(img)
    elif (a == 2):
        img = cv2.resize(img, (100 * 2, 100 * 2), interpolation=cv2.INTER_CUBIC)
        img_load(img)
    elif (a == 3):
        img = cv2.warpAffine(img, M, (width, height))
        img_load(img)
else:
    print("No exist file name")

"""
"""
import torch

dtype = torch.float

device = torch.device("cpu")

N, D_in,H, D_out = 64,1000,100,10

x = torch.randn(N,D_in, device=device, dtype=dtype)
y = torch.randn(N,D_out, device=device, dtype=dtype)

w1 = torch.randn(D_in,H, device=device, dtype=dtype)
w2 = torch.randn(H,D_out, device=device, dtype=dtype)

learning_rate = 1e-6

for t in range(500):

    h = x.mm(w1)

    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)

    loss = (y_pred - y).pow(2).sum().item()

    print(t, loss)

    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)

    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()

    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
"""
"""
import torch

dtype = torch.float

device = torch.device("cpu")

N, D_in,H, D_out = 64,1000,100,10

x = torch.randn(N,D_in, device=device, dtype=dtype)
y = torch.randn(N,D_out, device=device, dtype=dtype)

w1 = torch.randn(D_in,H, device=device, dtype=dtype, requires_grad = True)
w2 = torch.randn(H,D_out, device=device, dtype=dtype, requires_grad = True)

learning_rate = 1e-6

for t in range(500):

    y_pred = x.mm(w1).clamp(min=0).mm(w2)

    loss = (y_pred - y).pow(2).sum()

    print(t, loss.item())

    loss.backward()

    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        w2 -= learning_rate * w2.grad

        w1.grad.zero_()
        w2.grad.zero_()
"""
"""
import torch

N,D_in,H,D_out = 64,1000,100,10

x = torch.randn(N,D_in)
y = torch.randn(N,D_out)

model = torch.nn.Sequential(
    torch.nn.Linear(D_in,H),
    torch.nn.ReLU(),
    torch.nn.Linear(H,D_out)
)

loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4

for t in range(500):

    y_pred = model(x)

    loss = loss_fn(y_pred,y)

    print(t, loss.item())

    model.zero_grad()

    loss.backward()

    with torch.no_grad():

        for param in model.parameters():
            param -= learning_rate * param.grad
"""
"""
import torch

N,D_in,H,D_out = 64,1000,100,10

x = torch.randn(N,D_in)
y = torch.randn(N,D_out)

model = torch.nn.Sequential(
    torch.nn.Linear(D_in,H),
    torch.nn.ReLU(),
    torch.nn.Linear(H,D_out)
)

loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4

optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

for t in range(500):

    y_pred = model(x)

    loss = loss_fn(y_pred,y)

    print(t, loss.item())

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
"""
"""
import torch

class TwoLayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):

        super(TwoLayerNet,self).__init__()
        self.linear1 = torch.nn.Linear(D_in,H)
        self.linear2 = torch.nn.Linear(H, D_out)

    def forward(self, x):

        h_relu = self.linear1(x).clamp(min=0)
        y_pred = self.linear2(h_relu)

        return y_pred

N,D_in,H,D_out = 64,1000,100,10

x = torch.randn(N,D_in)
y = torch.randn(N,D_out)

model = TwoLayerNet(D_in,H,D_out)

criterion = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4

optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)

for t in range(500):

    y_pred = model(x)

    loss = criterion(y_pred,y)

    print(t, loss.item())

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
"""
import torch

from Two import TwoLayerNet

N,D_in,H,D_out = 64,1000,100,10

x = torch.randn(N,D_in)
y = torch.randn(N,D_out)

model = TwoLayerNet(D_in,H,D_out)

criterion = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4

optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)

for t in range(500):

    y_pred = model(x)

    loss = criterion(y_pred,y)

    print(t, loss.item())

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()'''

a,b,c = map(int,input().split())
d = int(input())

hour = int(d/3600)
min = int(d/60)
sec = d - (hour * 3600) - (min*60)

print("%.0f %.0f %.0f"%(x,y,z))
"""
