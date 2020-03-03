from tqdm import tqdm
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
import torchvision
import torchvision.transforms as transforms

def train(model, device, trainloader, optimizer, epochs,criterion):
	for epoch in range(epochs):  # loop over the dataset multiple times

	    running_loss = 0.0
	    for i, (data,target) in enumerate(trainloader):
	        # get the inputs
	        inputs, labels = data.to(device),target.to(device)

	        # zero the parameter gradients
	        optimizer.zero_grad()

	        # forward + backward + optimize
	        outputs = model(inputs)
	        loss = criterion(outputs, labels)
	        loss.backward()
	        optimizer.step()

	        # print statistics
	        running_loss += loss.item()
	        if i % 2000 == 1999:    # print every 2000 mini-batches
	            print('[%d, %5d] loss: %.3f' %
	                  (epoch + 1, i + 1, running_loss / 2000))
	            running_loss = 0.0

	print('Finished Training')