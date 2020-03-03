from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

def addConv2d(in_channels=1, out_channels=16, kernel_size=(3, 3),stride=1, padding=0,dilation=1, groups=1,
                 bias=True, padding_mode='zeros'):
	return nn.Conv2d(in_channels, out_channels, kernel_size,stride, padding,dilation, groups,
                 bias, padding_mode)