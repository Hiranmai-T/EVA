from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

def addActivation(name,inplace=False):
	if name=="relu":
		return nn.ReLU(inplace)