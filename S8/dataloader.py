import torch
import torchvision
import torchvision.transforms as transforms
#mean, std, inplace=False

def initialize_transforms(mean, std, inplace=False):
	transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize(mean, std)])
def dataloader(dataset,mean,nw, std,bs,use_cuda,inplace=False):
	kwargs = {'num_workers': nw, 'pin_memory': True} if use_cuda else {}
	transform = transforms.Compose(
    [transforms.RandomCrop(32, padding=4),
    transforms.RandomVerticalFlip(),
     transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
	if dataset=="cifar10":
		trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
		trainloader = torch.utils.data.DataLoader(trainset, batch_size=bs,
                                           shuffle=True,**kwargs)

		testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
		testloader = torch.utils.data.DataLoader(testset, batch_size=bs-28,
                                          shuffle=False,**kwargs)
		return trainset,trainloader,testset,testloader