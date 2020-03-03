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
