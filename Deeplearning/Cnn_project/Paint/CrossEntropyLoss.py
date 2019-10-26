from Deeplearning.Cnn_project.Paint.temp_model import TrModel
import torch
from Deeplearning.Cnn_project.Paint.bri053 import NKDataSet

csv_path = './data_load/data_load.csv'

custom_dataset = NKDataSet(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset= custom_dataset,
                                                batch_size=5,
                                                shuffle=False,
                                                )

model = TrModel(30000,100,5)

criterion = torch.nn.CrossEntropyLoss(reduction = 'sum')
optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)

for t in range(500):
    for i, data in enumerate(my_dataset_loader, 0):

        images, label = data
        images = images.view(5, 30000)
        #print(images.size())
        #print("label is label", label)
        y_pred = model(images)
        loss = criterion(y_pred, label)
        print(t, loss.item())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()