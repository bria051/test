from torch.utils.data.dataset import Dataset
import torch
from test_3 import Cnn_Model
from test_2 import NKDataSet


#cnn_model,my_dataset
def train(my_dataset_loader,model,criterion,optimizer,epoch):

    model.train()

    for x, data in enumerate(my_dataset_loader, 0):

        images,label = data

        print(images.size())
        y_pred = model(images)

        print(y_pred)

        loss = criterion(y_pred, label)

        print(epoch, loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def test(my_dataset_loader, model,criterion, epoch):

    model.eval()

    for x, data in enumerate(my_dataset_loader, 0):

        images, label = data


        y_pred = model(images)

        loss = criterion(y_pred, label)

        print(epoch, loss.item())

csv_path = './data_load/data_load.csv'

custom_dataset = NKDataSet(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset = custom_dataset,
                                               batch_size = 5,
                                               shuffle = False,
                                               num_workers = 1)

D_in = 30000
H = 100
D_out = 6

model = Cnn_Model()

crierion = torch.nn.CrossEntropyLoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)

for epoch in range(500):

    print('epoch',epoch)

    train(my_dataset_loader,model,crierion,optimizer,epoch)
    test(my_dataset_loader,model,crierion,epoch)