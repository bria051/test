from torch.utils.data.dataset import Dataset
import torch
from Deeplearning.Cnn_project.Paint.Cnn_Model import Cnn_Model
from Deeplearning.Cnn_project.Paint.bri053 import NKDataSet
from tensorboardX import SummaryWriter
import argparse
import time
import os

parser = argparse.ArgumentParser(description='PyTorch Custom Training')
parser.add_argument('--print_freq','--p',default=2,type=int,metavar='N',
                    help='number of data loading workers (default: 4)')
parser.add_argument('--save-import torch.nn.init as initdir',dest='save_dir',help='The directory used to save the trained models'
                                                                                ,default='save_layer_load',type=str)
args = parser.parse_args()

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

    batch_time = AverageMeter()
    data_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()

    for i, data in enumerate(my_dataset_loader, 0):

        images, label = data

        images = torch.autograd.Variable(images)
        label = torch.autograd.Variable(label)

        y_pred = model(images)

        loss = criterion(y_pred,label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        output = y_pred.float()
        loss = loss.float()

        prec1 = accuracy(output.data, label)[0]

        prec_2 = accuracy(output.data, label)

        losses.update(loss.item(), images.size(0))
        top1.update(prec1.item(), images.size(0))

    writer.add_scalar('Train/loss',losses.avg, epoch)
    writer.add_scalar('Train/accuaracy', top1.avg, epoch)

def test(my_dataset_loader, model, criterion, epoch, test_writer):

    losses = AverageMeter()
    top1 = AverageMeter()
    model.eval()

    batch_time = AverageMeter()
    end = time.time()

    for i, data in enumerate(my_dataset_loader, 0):

        images, label = data

        y_pred = model(images)

        loss = criterion(y_pred, label)

        output = y_pred.float()
        loss = loss.float()

        prec1 = accuracy(output.data, label)[0]

        losses.update(loss.item(), images.size(0))
        top1.update(prec1.item(), images.size(0))

        batch_time.update(time.time() - end)
        end = time.time()

        if i % args.print_freq == 0:
            print('Test : [{0}/{1}\t'
                  'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                  'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                  'Prec@1 {top1.val:.3f} ({top1.avg:.3f})'.format(
                i,len(my_dataset_loader),batch_time=batch_time,loss=losses,top1=top1
            ))

    print(' *, epoch : {epoch:.2f} Prec@1 {top1.avg:.3f}'
          .format(epoch = epoch,top1= top1))

    test_writer.add_scalar('Test/loss', losses.avg, epoch)
    test_writer.add_scalar('Test/accuaracy', top1.avg, epoch)

csv_path = './data_load/data_load.csv'

custom_dataset = NKDataSet(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=5,
                                                shuffle=True,
                                                num_workers=1)

D_in = 30000
H = 100
H = 100
D_out = 2

model = Cnn_Model()

checkpoint = torch.load('save_dir/checkpoint_2.tar')
model.load_state_dict(checkpoint['state_dict'])


criterion = torch.nn.CrossEntropyLoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(),lr=1e-2)

writer = SummaryWriter('./log')
test_writer = SummaryWriter('.log/test')

args.save_dir = 'save_dir'

for epoch in range(500):
    train(my_dataset_loader,model,criterion,optimizer,epoch,writer)
    test(my_dataset_loader,model,criterion,epoch,test_writer)

    save_checkpoint({'epoch': epoch + 1,
                     'state_dict': model.state_dict(),
            }, filename=os.path.join(args.save_dir, 'checkpoint_{}.tar'.format(epoch)))

