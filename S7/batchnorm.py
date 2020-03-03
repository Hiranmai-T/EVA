from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

def addBatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True):
	return nn.BatchNorm2d(num_features, eps, momentum, affine, track_running_stats)