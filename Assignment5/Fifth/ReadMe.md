Target: To still increase the accuracy by changing lr_scheduler if possible

Result: After changing the step to 4 and lr to 0.03, the model was able to achieve 99.46% accuracy in
the 12th epoch and the last few epochs are close to 99.4% accuracy.

EPOCH: 12
Loss=0.03359299153089523 Batch_id=468 Accuracy=98.84: 100%|██████████| 469/469 [00:14<00:00, 31.32it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0173, Accuracy: 9946/10000 (99.46%)

Analysis: Instead of reducing the step to 5 as before, I have reduced it to 4 here based on the logs. There is no overfitting in the model.
But I think it can be pushed further

Code Link:https://colab.research.google.com/drive/12I1jeex-BrOJ90Xchbs7SjI-bY1agQio
