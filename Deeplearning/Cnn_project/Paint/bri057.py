import torch

batch_size = 2
class Regression_model(torch.nn.Module):

    def __init__(self):

        super(Regression_model, self).__init__()
        self.conv1 = torch.nn.Conv2d(3,20,kernel_size = 3)
        self.relu = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(20,2,kernel_size = 3)
        self.conv3 = torch.nn.Linear(18432,1)

    def forward(self, x):

        x = self.conv1(x)
        print(x.size())
        x = self.relu(x)
        x = self.conv2(x)
        print(x.size())
        x = self.relu(x)
        x = x.view(batch_size,-1)
        print(x.size())
        x = self.conv3(x)

        return x