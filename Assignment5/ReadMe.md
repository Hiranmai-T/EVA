**Approach:**

Step1: I have taken the approach of colab 10 in session, and ran it for 15 epochs to see its performance. It has achieved 99.48% in the
9th epoch.But the parameters were 13,808. So my next step was to reduce the number of parameters.

(Assignment 5.1)

Colab Link:https://colab.research.google.com/drive/1Z6s8I1dEUnQ9zex19t-oTThQ7eTLYOrj

Step2: After making some changes in the architecture, I was able to achieve 9812 parameters. There were no other changes in the rest of the code.
This model achieved 99.42% in its 10th epoch, but it was the only time it was able to achieve it. So I thought maybe change the lr_scheduler!

(Assignment 5.2)

Colab Link:https://colab.research.google.com/drive/1nwoHb7uCNaI_PsTFgmz4eJJV9kPvlI_u

Step3: After watching the logs of the previous file, I decided to decrease my step to 5 and changed the learning rate to 0.03. I tried the same
with Adam Scheduler but the results were not what was desired. So i stuck to SGD optimizer.

Colab Link: https://colab.research.google.com/drive/1_h_eDEuatSFbjg7OMOGAThrVIEIjq0Fv

The last few logs are as follows:(Assignment 5.3)
EPOCH: 11 \n
Loss=0.04909350350499153 Batch_id=468 Accuracy=98.84: 100%|██████████| 469/469 [00:14<00:00, 32.79it/s] \n
  0%|          | 0/469 [00:00<?, ?it/s] \n
Test set: Average loss: 0.0195, Accuracy: 9943/10000 (99.43%) \n

EPOCH: 12
Loss=0.05696297809481621 Batch_id=468 Accuracy=98.85: 100%|██████████| 469/469 [00:14<00:00, 33.07it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0187, Accuracy: 9939/10000 (99.39%)

EPOCH: 13
Loss=0.06801556795835495 Batch_id=468 Accuracy=98.89: 100%|██████████| 469/469 [00:14<00:00, 32.83it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0213, Accuracy: 9934/10000 (99.34%)

EPOCH: 14
Loss=0.005450303200632334 Batch_id=468 Accuracy=98.94: 100%|██████████| 469/469 [00:14<00:00, 33.64it/s]

Test set: Average loss: 0.0207, Accuracy: 9936/10000 (99.36%)

The model was not over fitting, but the accuracy has to be more consistent.

Step 4: After that I have started to think about various data transformations I could do. First I started with random Horizontal flip.
The results were not good at all. I think this is so because, on numbers like 1, horizantal flip would be good, there wont be any images 
in our dataset where the numbers will be flipped. So i made the model hard unnecessarily. Even random erasing could not fetch much results.

Colab Link:https://colab.research.google.com/drive/1DHtQcx62YI_DWHHYapGQtoUqZkl3mczD

(Assignment 5.4)

Step 5: I started playing with the lr_schedulers. I thought why not reduce the step one more down to 4. And the results were similar to step3.
The last few logs are as follows:(Assignment5.6)

Colab Link:https://colab.research.google.com/drive/12I1jeex-BrOJ90Xchbs7SjI-bY1agQio

EPOCH: 11
Loss=0.06990917772054672 Batch_id=468 Accuracy=98.82: 100%|██████████| 469/469 [00:15<00:00, 29.76it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0188, Accuracy: 9939/10000 (99.39%)

EPOCH: 12
Loss=0.03359299153089523 Batch_id=468 Accuracy=98.84: 100%|██████████| 469/469 [00:14<00:00, 31.32it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0173, Accuracy: 9946/10000 (99.46%)

EPOCH: 13
Loss=0.022327685728669167 Batch_id=468 Accuracy=98.87: 100%|██████████| 469/469 [00:14<00:00, 31.66it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0192, Accuracy: 9944/10000 (99.44%)

EPOCH: 14
Loss=0.008584350347518921 Batch_id=468 Accuracy=98.90: 100%|██████████| 469/469 [00:14<00:00, 31.56it/s]

Test set: Average loss: 0.0196, Accuracy: 9938/10000 (99.38%)
  
