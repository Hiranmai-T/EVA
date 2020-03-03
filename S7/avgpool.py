from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

def addAvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None):
	return nn.AvgPool2d(kernel_size, stride, padding, ceil_mode, count_include_pad, divisor_override)