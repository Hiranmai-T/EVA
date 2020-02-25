# Misclassifications

**While using L1**
![L1_misclassifications](https://github.com/Hiranmai-T/EVA/blob/master/S6/mis_l1.png)

**While using L2**
![L2_misclassifications](https://github.com/Hiranmai-T/EVA/blob/master/S6/mis_l2.png)

## Validation accuracy change graph
![acc_graph](https://github.com/Hiranmai-T/EVA/blob/master/S6/graph_acc.png)

## Loss change graph
![loss_graph](https://github.com/Hiranmai-T/EVA/blob/master/S6/graph_loss.png)

## Analysis

L1 and L2 act as reguralization techniques and help us overcome over fitting. By seeing the above graphs, I can see that there is no big change in accuracy when I was not using L1 and L2 and when I was using them. And picking the value of lambda is also important and depends on the dataset. When I used lambda as 0.5 for L1, the accuracy decreased drastically as it is giving more weight to the L1 regularization term. When both are combinely used the accuracy decreased. I think the model is not overfitting to a large extent as there is little differnce to when L1 is used and not used. 



**Some Pointers:** in L1 regularization there is still a push to squish even small weights towards zero, more so than in L2 regularization.
