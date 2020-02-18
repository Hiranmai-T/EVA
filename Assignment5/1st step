Target : To understand what happens when the same model in colab 10 would work under 15 epochs

Result: It gave 99.48% in the 19th epoch. And the 99.4% was consistent in the last few epochs.

EPOCH: 9
Loss=0.02939785085618496 Batch_id=468 Accuracy=98.90: 100%|██████████| 469/469 [00:15<00:00, 31.19it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0179, Accuracy: 9948/10000 (99.48%)

Analysis: Dropout and batch normalization has been added to each layer but the last layer here. Adding dropout reduces the number of paramters here.
The model is good given the number of parameters which is 13k. Now the task is to reduce the number of parameters. 
The first block which I see with high number of parameters is conv7 block with 2k parameters.

File Link: https://colab.research.google.com/drive/1Z6s8I1dEUnQ9zex19t-oTThQ7eTLYOrj
