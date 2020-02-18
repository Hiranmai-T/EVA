Target: To look for ways to increase the accuracy further by doing data augmentation.

Result: I have used horizontal flip and the accuracy decreased.

EPOCH: 12
Loss=0.02799469232559204 Batch_id=468 Accuracy=97.07: 100%|██████████| 469/469 [00:14<00:00, 31.33it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0557, Accuracy: 9818/10000 (98.18%)


Analysis: It was silly to use horizontal flip, as there will be no digits written in the dataset by 
flipping them, the only digit which can be flipped is 1. So this is not the data augmentation which is required.

Code Link : https://colab.research.google.com/drive/1DHtQcx62YI_DWHHYapGQtoUqZkl3mczD 
