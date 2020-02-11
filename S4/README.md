Colab Link: https://colab.research.google.com/drive/1t0Vx5guegkrE1uZniGjk46f_js2M2NV- 

**Model Parameters**

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================

            Conv2d-1           [-1, 16, 26, 26]             160
            
       BatchNorm2d-2           [-1, 16, 26, 26]              32
       
         Dropout2d-3           [-1, 16, 26, 26]               0
         
            Conv2d-4           [-1, 32, 24, 24]           4,640
            
       BatchNorm2d-5           [-1, 32, 24, 24]              64
       
         Dropout2d-6           [-1, 32, 24, 24]               0
         
            Conv2d-7           [-1, 10, 24, 24]             330
            
         MaxPool2d-8           [-1, 10, 12, 12]               0
         
            Conv2d-9           [-1, 16, 10, 10]           1,456
            
      BatchNorm2d-10           [-1, 16, 10, 10]              32
      
        Dropout2d-11           [-1, 16, 10, 10]               0
        
           Conv2d-12             [-1, 16, 8, 8]           2,320
           
      BatchNorm2d-13             [-1, 16, 8, 8]              32
      
        Dropout2d-14             [-1, 16, 8, 8]               0
        
           Conv2d-15             [-1, 16, 6, 6]           2,320
           
      BatchNorm2d-16             [-1, 16, 6, 6]              32
      
        Dropout2d-17             [-1, 16, 6, 6]               0
        
           Conv2d-18             [-1, 16, 4, 4]           2,320
           
      BatchNorm2d-19             [-1, 16, 4, 4]              32
      
        Dropout2d-20             [-1, 16, 4, 4]               0
        
           Conv2d-21             [-1, 10, 4, 4]             170
           
           Conv2d-22             [-1, 10, 1, 1]           1,610
           
================================================================
Total params: 15,550
Trainable params: 15,550
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.80
Params size (MB): 0.06
Estimated Total Size (MB): 0.87








0%|          | 0/469 [00:00<?, ?it/s]/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:59: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.
loss=0.09419889003038406 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.55it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0539, Accuracy: 9828/10000 (98%)

loss=0.023708820343017578 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.77it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0450, Accuracy: 9849/10000 (98%)

loss=0.04059842601418495 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.69it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0421, Accuracy: 9875/10000 (99%)

loss=0.07449846714735031 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 34.68it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0322, Accuracy: 9894/10000 (99%)

loss=0.10797397047281265 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.27it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0314, Accuracy: 9897/10000 (99%)

loss=0.08794645220041275 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.38it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0270, Accuracy: 9912/10000 (99%)

loss=0.07736221700906754 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 33.82it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0314, Accuracy: 9912/10000 (99%)

loss=0.049742117524147034 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.84it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0272, Accuracy: 9918/10000 (99%)

loss=0.03201547637581825 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.62it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0265, Accuracy: 9919/10000 (99%)

loss=0.0686965063214302 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 30.03it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0306, Accuracy: 9907/10000 (99%)

loss=0.032973576337099075 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 34.09it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0301, Accuracy: 9914/10000 (99%)

loss=0.006199732422828674 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.56it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0315, Accuracy: 9907/10000 (99%)

loss=0.04234200343489647 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 33.46it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0234, Accuracy: 9925/10000 (99%)

loss=0.07508610934019089 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.51it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0266, Accuracy: 9924/10000 (99%)

loss=0.029243728145956993 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.07it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0255, Accuracy: 9925/10000 (99%)

loss=0.08331248909235 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 31.52it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0239, Accuracy: 9933/10000 (99%)

loss=0.0443134605884552 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 31.73it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0250, Accuracy: 9931/10000 (99%)

**loss=0.050017643719911575 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 31.42it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0218, Accuracy: 9940/10000 (99%)**

loss=0.014100599102675915 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.80it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0242, Accuracy: 9932/10000 (99%)

loss=0.1070404052734375 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.61it/s]

Test set: Average loss: 0.0265, Accuracy: 9924/10000 (99%)

