**Model Architecture**


Requirement already satisfied: torchsummary in /usr/local/lib/python3.6/dist-packages (1.5.1)

----------------------------------------------------------------

        Layer (type)               Output Shape         Param #
        
================================================================

            Conv2d-1           [-1, 32, 32, 32]             864
            
              ReLU-2           [-1, 32, 32, 32]               0
              
       BatchNorm2d-3           [-1, 32, 32, 32]              64
       
           Dropout-4           [-1, 32, 32, 32]               0
           
            Conv2d-5           [-1, 64, 24, 24]          18,432
            
              ReLU-6           [-1, 64, 24, 24]               0
              
       BatchNorm2d-7           [-1, 64, 24, 24]             128
       
           Dropout-8           [-1, 64, 24, 24]               0
           
         MaxPool2d-9           [-1, 64, 12, 12]               0
         
           Conv2d-10          [-1, 128, 12, 12]          36,864
           
             ReLU-11          [-1, 128, 12, 12]               0
             
      BatchNorm2d-12          [-1, 128, 12, 12]             256
      
          Dropout-13          [-1, 128, 12, 12]               0
          
           Conv2d-14           [-1, 64, 14, 14]           8,192
           
        MaxPool2d-15             [-1, 64, 7, 7]               0
        
           Conv2d-16            [-1, 128, 3, 3]          73,728
           
             ReLU-17            [-1, 128, 3, 3]               0
             
      BatchNorm2d-18            [-1, 128, 3, 3]             256
      
          Dropout-19            [-1, 128, 3, 3]               0
          
        MaxPool2d-20            [-1, 128, 1, 1]               0
        
           Conv2d-21             [-1, 64, 1, 1]           8,192
           
        AvgPool2d-22             [-1, 64, 1, 1]               0
        
           Conv2d-23             [-1, 10, 1, 1]             640
           
================================================================

Total params: 147,616

Trainable params: 147,616

Non-trainable params: 0

----------------------------------------------------------------

Input size (MB): 0.01

Forward/backward pass size (MB): 2.91

Params size (MB): 0.56

Estimated Total Size (MB): 3.49

----------------------------------------------------------------

**Logs for 50 Epochs**(But ran for only 35 epochs, colab ram exceeded)

  0%|          | 0/12500 [00:00<?, ?it/s]EPOCH: 0
Loss=1.9553799629211426 Batch_id=12499 Accuracy=45.30: 100%|██████████| 12500/12500 [01:55<00:00, 108.07it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.4679, Accuracy: 5321/10000 (53.21%)

EPOCH: 1
Loss=1.6963998079299927 Batch_id=12499 Accuracy=56.61: 100%|██████████| 12500/12500 [01:55<00:00, 108.18it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.4034, Accuracy: 5966/10000 (59.66%)

EPOCH: 2
Loss=2.141896963119507 Batch_id=12499 Accuracy=60.94: 100%|██████████| 12500/12500 [01:55<00:00, 108.47it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.3747, Accuracy: 6253/10000 (62.53%)

EPOCH: 3
Loss=1.3438788652420044 Batch_id=12499 Accuracy=64.90: 100%|██████████| 12500/12500 [01:55<00:00, 108.39it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.3445, Accuracy: 6555/10000 (65.55%)

EPOCH: 4
Loss=0.42579594254493713 Batch_id=12499 Accuracy=67.02: 100%|██████████| 12500/12500 [01:55<00:00, 108.17it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.3353, Accuracy: 6647/10000 (66.47%)

EPOCH: 5
Loss=0.9640254378318787 Batch_id=12499 Accuracy=69.17: 100%|██████████| 12500/12500 [01:56<00:00, 107.71it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.3404, Accuracy: 6596/10000 (65.96%)

EPOCH: 6
Loss=0.6508973240852356 Batch_id=12499 Accuracy=71.03: 100%|██████████| 12500/12500 [01:55<00:00, 108.21it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.3280, Accuracy: 6720/10000 (67.20%)

EPOCH: 7
Loss=0.47116971015930176 Batch_id=12499 Accuracy=72.02: 100%|██████████| 12500/12500 [01:55<00:00, 108.23it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.3057, Accuracy: 6943/10000 (69.43%)

EPOCH: 8
Loss=0.3969659209251404 Batch_id=12499 Accuracy=72.96: 100%|██████████| 12500/12500 [01:54<00:00, 108.71it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.3099, Accuracy: 6901/10000 (69.01%)

EPOCH: 9
Loss=0.7617626190185547 Batch_id=12499 Accuracy=73.80: 100%|██████████| 12500/12500 [01:55<00:00, 108.13it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2996, Accuracy: 7004/10000 (70.04%)

EPOCH: 10
Loss=0.4780879616737366 Batch_id=12499 Accuracy=74.62: 100%|██████████| 12500/12500 [01:55<00:00, 108.49it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2904, Accuracy: 7096/10000 (70.96%)

EPOCH: 11
Loss=0.7871376872062683 Batch_id=12499 Accuracy=75.59: 100%|██████████| 12500/12500 [01:54<00:00, 108.74it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.3029, Accuracy: 6971/10000 (69.71%)

EPOCH: 12
Loss=0.733571469783783 Batch_id=12499 Accuracy=76.21: 100%|██████████| 12500/12500 [01:56<00:00, 107.42it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2946, Accuracy: 7054/10000 (70.54%)

EPOCH: 13
Loss=0.9347314834594727 Batch_id=12499 Accuracy=76.60: 100%|██████████| 12500/12500 [01:55<00:00, 108.09it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2941, Accuracy: 7059/10000 (70.59%)

EPOCH: 14
Loss=1.3118540048599243 Batch_id=12499 Accuracy=77.41: 100%|██████████| 12500/12500 [01:55<00:00, 107.90it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2852, Accuracy: 7148/10000 (71.48%)

EPOCH: 15
Loss=0.4044226408004761 Batch_id=12499 Accuracy=78.07: 100%|██████████| 12500/12500 [01:55<00:00, 107.96it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2808, Accuracy: 7192/10000 (71.92%)

EPOCH: 16
Loss=0.34429746866226196 Batch_id=12499 Accuracy=78.40: 100%|██████████| 12500/12500 [01:56<00:00, 107.12it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2668, Accuracy: 7332/10000 (73.32%)

EPOCH: 17
Loss=1.4686015844345093 Batch_id=12499 Accuracy=78.93: 100%|██████████| 12500/12500 [01:56<00:00, 107.02it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2784, Accuracy: 7216/10000 (72.16%)

EPOCH: 18
Loss=0.7041420936584473 Batch_id=12499 Accuracy=79.18: 100%|██████████| 12500/12500 [01:55<00:00, 108.40it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2678, Accuracy: 7322/10000 (73.22%)

EPOCH: 19
Loss=0.46316733956336975 Batch_id=12499 Accuracy=79.64: 100%|██████████| 12500/12500 [01:56<00:00, 107.62it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2685, Accuracy: 7315/10000 (73.15%)

EPOCH: 20
Loss=0.6154664754867554 Batch_id=12499 Accuracy=80.02: 100%|██████████| 12500/12500 [01:55<00:00, 108.54it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2632, Accuracy: 7368/10000 (73.68%)

EPOCH: 21
Loss=0.8798267841339111 Batch_id=12499 Accuracy=80.22: 100%|██████████| 12500/12500 [01:55<00:00, 108.69it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2753, Accuracy: 7247/10000 (72.47%)

EPOCH: 22
Loss=0.03658173605799675 Batch_id=12499 Accuracy=80.81: 100%|██████████| 12500/12500 [01:55<00:00, 108.09it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2720, Accuracy: 7280/10000 (72.80%)

EPOCH: 23
Loss=0.26351431012153625 Batch_id=12499 Accuracy=81.10: 100%|██████████| 12500/12500 [01:54<00:00, 108.91it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2631, Accuracy: 7369/10000 (73.69%)

EPOCH: 24
Loss=0.7107751369476318 Batch_id=12499 Accuracy=81.19: 100%|██████████| 12500/12500 [01:55<00:00, 108.25it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2665, Accuracy: 7335/10000 (73.35%)

EPOCH: 25
Loss=0.669184684753418 Batch_id=12499 Accuracy=81.57: 100%|██████████| 12500/12500 [01:56<00:00, 107.02it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2587, Accuracy: 7413/10000 (74.13%)

EPOCH: 26
Loss=0.5714967846870422 Batch_id=12499 Accuracy=81.84: 100%|██████████| 12500/12500 [01:55<00:00, 107.99it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2605, Accuracy: 7395/10000 (73.95%)

EPOCH: 27
Loss=0.6295639276504517 Batch_id=12499 Accuracy=82.26: 100%|██████████| 12500/12500 [01:56<00:00, 107.74it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2625, Accuracy: 7375/10000 (73.75%)

EPOCH: 28
Loss=0.7261045575141907 Batch_id=12499 Accuracy=82.17: 100%|██████████| 12500/12500 [01:55<00:00, 107.86it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2586, Accuracy: 7414/10000 (74.14%)

EPOCH: 29
Loss=0.3115461468696594 Batch_id=12499 Accuracy=82.51: 100%|██████████| 12500/12500 [01:55<00:00, 107.95it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2629, Accuracy: 7371/10000 (73.71%)

EPOCH: 30
Loss=1.894353985786438 Batch_id=12499 Accuracy=82.74: 100%|██████████| 12500/12500 [01:57<00:00, 106.75it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2647, Accuracy: 7353/10000 (73.53%)

EPOCH: 31
Loss=1.0158209800720215 Batch_id=12499 Accuracy=82.97: 100%|██████████| 12500/12500 [01:55<00:00, 107.79it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2710, Accuracy: 7290/10000 (72.90%)

EPOCH: 32
Loss=0.08009141683578491 Batch_id=12499 Accuracy=83.20: 100%|██████████| 12500/12500 [01:56<00:00, 107.39it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2628, Accuracy: 7372/10000 (73.72%)

EPOCH: 33
Loss=0.5477630496025085 Batch_id=12499 Accuracy=83.54: 100%|██████████| 12500/12500 [01:55<00:00, 108.28it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2703, Accuracy: 7297/10000 (72.97%)

EPOCH: 34
Loss=0.11709010601043701 Batch_id=12499 Accuracy=83.71: 100%|██████████| 12500/12500 [01:55<00:00, 108.21it/s]
  0%|          | 0/12500 [00:00<?, ?it/s]
Test set: Average loss: 0.2584, Accuracy: 7416/10000 (74.16%)

EPOCH: 35
Loss=0.6508391499519348 Batch_id=6886 Accuracy=83.97:  55%|█████▌    | 6876/12500 [01:04<00:51, 110.04it/s]

**Max Accuracy till now:** 74.16%
