
import torch

class TrModel(torch.nn.Module):

    def __init__(self,D_in, H, D_out):

        super(TrModel,self).__init__()
        self.linear1 = torch.nn.Linear(D_in,H)
        self.linear2 = torch.nn.Linear(H,D_out)

    def forward(self, x):

        h_relu = self.linear1(x).clamp(min=0)
        y_pred = self.linear2(h_relu)

        return y_pred

"""

bias = 2

a = 3
b = 5
c = 2

blueline = 0.1
blueline2 = 0.2
blueline3 = 0.3

redline = 0.4
redline1 = 0.5
redline2 = 0.6

def cal_temp(a,b,c):

    d = a,b,c*blueline,blueline2,blueline3+bias
    e = a,b,c*redline,redline1,redline2+bias

    return d,e

temp = cal_temp(a,b,c)
"""
