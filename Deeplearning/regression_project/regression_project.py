#regression project
from torch.utils.data.dataset import Dataset
import torch
from Deeplearning.Cnn_project.Paint.bri057 import Regression_model
from Deeplearning.Cnn_project.Paint.bri053 import NKDataSet
from tensorboardX import SummaryWriter
import os

def save_checkpoint(state,filename='checkpoint.pth.bar'):
    torch.save(state,filename)

def accuracy(output, target, topk=(1, )):
    maxk = max(topk)
    batch_size = target.size(0)

    _,pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1,-1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))

    return res
class AverageMeter(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self,val,n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

def train(my_dataset_loader,model,criterion,optimizer,epoch,writer):
    model.train()
    losses = AverageMeter()
    for i, data in enumerate(my_dataset_loader, 0):

        images, label = data
        images = torch.autograd.Variable(images)
        label = torch.autograd.Variable(label).float()
        y_pred = model(images)
        loss = criterion(y_pred,label)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss = loss.float()
        losses.update(loss.item(), images.size(0))

    losses = AverageMeter()

    for i, data in enumerate(my_dataset_loader, 0):

        images, label = data

        images = torch.autograd.Variable(images)
        label = torch.autograd.Variable(label).float()

        y_pred = model(images)

        loss = criterion(y_pred,label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        loss = loss.float()



        losses.update(loss.item(), images.size(0))
    writer.add_scalar('Train/loss',losses.avg, epoch)


def test(my_dataset_loader, model, criterion, epoch, test_writer):

    losses = AverageMeter()

    model.eval()
    for i, data in enumerate(my_dataset_loader, 0):

        images, label = data
        y_pred = model(images)
        label = label.float()
        loss = criterion(y_pred, label)
        loss = loss.float()
        losses.update(loss.item(), images.size(0))


    print(' *, epoch : {epoch:.2f} Prec@1 {losses .avg:.3f}'
          .format(epoch = epoch,losses=losses))

    test_writer.add_scalar('Test/loss', losses.avg, epoch)

csv_path = './data_load/train.csv'
custom_dataset = NKDataSet(csv_path)

csv_path = './data_load/data_load.csv'

custom_dataset = NKDataSet(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=2,
                                                shuffle=True,
                                                num_workers=1)
csv_path = './data_load/test.csv'
custom_dataset = NKDataSet(csv_path)
test_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=2,
                                                shuffle=True,
                                                num_workers=1)
model = Regression_model()
criterion = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(),lr=1e-1)

writer = SummaryWriter('./log_2')
test_writer = SummaryWriter('.log_2/test')
for epoch in range(500):
    train(my_dataset_loader,model,criterion,optimizer,epoch,writer)
    test(test_dataset_loader,model,criterion,epoch,test_writer)

    save_checkpoint({'epoch': epoch + 1,
                     'state_dict': model.state_dict()
                     }, filename=os.path.join("./save_dir", 'checkpoint_{}.tar'.format(epoch)))

# 84199e+4(841,990,000)
# 10575e+5(1,057,500,000)

model = Regression_model()

criterion = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(),lr=1e-2)

writer = SummaryWriter('./log')
test_writer = SummaryWriter('.log/test')
for epoch in range(500):
    train(my_dataset_loader,model,criterion,optimizer,epoch,writer)
    test(my_dataset_loader,model,criterion,epoch,test_writer)
