import os, os.path
from temp_model import TrModel
import numpy as np
import cv2
import torch
from torchvision import transforms

img_sort = ['jpeg','.jpg','.png']
img_list = []

path = './data'


for x in range(len(img_sort)):
    for filename in os.listdir(path):
        if(filename.lower().endswith(img_sort[x])):
            print(filename)

            file = cv2.imread(filename)
            re_image = cv2.resize(file,(100,100))
            img_list.append(re_image)



img_arr = np.asarray(img_list)

img_as_tensor = []

for i in range(len(img_arr)):
    img = transforms.ToTensor()(img_arr[i])
    img = img.view(-1)
    img_as_tensor.append(img)

num_image = 2
num_class = 2

label = torch.empty(num_image, dtype = torch.long)

label[0] = 0
label[1] = 1


model = TrModel(30000,100,2)

criterion = torch.nn.CrossEntropyLoss(reduction = 'sum')
optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)

img_as_tensor = torch.stack(img_as_tensor)

print(img_as_tensor.size())
for t in range(500):

    y_pred = model(img_as_tensor)
    loss = criterion(y_pred, label)
    print(t, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
