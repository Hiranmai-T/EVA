import torch.nn as nn
import torch.nn.functional as F
from activation import addActivation
from avgpool import addAvgPool2d
from dropout import addDropout
from maxpool import addMaxPool2d
from batchnorm import addBatchNorm2d
from conv2d import addConv2d
import torch
import torchvision
import torchvision.transforms as transforms

dropout_value = 0.1
#torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros')
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.convblock1 = nn.Sequential(
            addConv2d(in_channels=3, out_channels=32, kernel_size=(3, 3),stride=1, padding=1, bias=False), #in=32  out =32 rf = 3 
            addActivation("relu"),
            addBatchNorm2d(32),
            addDropout(dropout_value)
        )
        self.convblock2 = nn.Sequential(
            addConv2d(in_channels=32, out_channels=64, kernel_size=(3, 3),stride=1,dilation=4, padding=0, bias=False), #in = 32  out = 24  rf = 11
            addActivation("relu"),
            addBatchNorm2d(64),
            addDropout(dropout_value)
        )
        #maxpool1
        self.pool1 = addMaxPool2d(2, 2)  #in=24  out = 12 rf = 13 
        
        
        self.convblock3 = nn.Sequential(
            addConv2d(in_channels=64, out_channels=128, kernel_size=(3, 3),stride=1,groups=2, padding=1, bias=False), #in= 12  out = 12 rf = 17
            addActivation("relu"),
            addBatchNorm2d(128),
            addDropout(dropout_value)
        )
        
        #Transition block1
        self.convblock4 = nn.Sequential(
           addConv2d(in_channels=128, out_channels=64, kernel_size=(1, 1), padding=1, bias=False), #in = 12  out = 14 rf = 17 
        )
        #maxpool2
        self.pool2 = addMaxPool2d(2, 2) #in = 14  out = 7 rf = 19

        self.convblock5 = nn.Sequential(
            addConv2d(in_channels=64, out_channels=128, kernel_size=(3, 3),stride=1,dilation=3, padding=1, bias=False), #in = 7 out = 3 rf = 43 (19+6*4)?
            addActivation("relu"),
            addBatchNorm2d(128),
            addDropout(dropout_value)
        )
        #maxpool3
        self.pool3 = addMaxPool2d(2, 2) #in = 3  out = 1 rf = 47
        self.convblock6 = nn.Sequential(
           addConv2d(in_channels=128, out_channels=64, kernel_size=(1, 1), padding=0, bias=False),
        )
        self.convblock7 = nn.Sequential(
            addAvgPool2d(kernel_size=1),
            addConv2d(in_channels=64, out_channels=10, kernel_size=(1, 1), padding=0, bias=False),
            
        )
       

    def forward(self, x):
        x = self.convblock1(x)
        x = self.convblock2(x)
        x = self.pool1(x)
        x = self.convblock3(x)
        x = self.convblock4(x)
        x = self.pool2(x)
        x = self.convblock5(x)
        x = self.pool3(x)
        x = self.convblock6(x)
        x = self.convblock7(x)
        x = x.view(-1,10)
        return F.log_softmax(x, dim=-1)
def initiate_model():
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    model = Net().to(device)
    return model