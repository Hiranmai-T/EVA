Target: To reduce the number of parameters to less than 10k

Result: I was able to do this, by removing conv7 block in previous step and reducing the computations slightly in 
transition block 1 and the conv block following that. Now the model has 9812 parameters.

EPOCH: 10
Loss=0.019986994564533234 Batch_id=468 Accuracy=98.73: 100%|██████████| 469/469 [00:14<00:00, 34.69it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0207, Accuracy: 9942/10000 (99.42%)

Analysis: The model gave 99.42% accuracy in the 10th epoch. But that is the only time, the accuracy went over 99.4% 
But this is to be expected because I have reduced the number of parameters from the previous model. 
Now I have to look at different places from where I can compensate this loss of parameters

Code Link: https://colab.research.google.com/drive/1nwoHb7uCNaI_PsTFgmz4eJJV9kPvlI_u
