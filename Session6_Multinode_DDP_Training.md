Below are details of multinode DDP training for CIFAR10 and VIT224

GPU nodes: 2
Type: G4dn.xlarge
Strategy: DDP

Train stats:
Batch size: 256
LR: 0.0001

Trainable params: 87.5 M                                                                                
Non-trainable params: 0                                                                                 
Total params: 87.5 M                                                                                    
Total estimated model params size (MB): 349                                                             
Epoch 0    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0/98 0:00:00 • -:--:-- 0.00it/s loss: nan v_num: 0 val/acc:   
                                                                          0.093 val/acc_best: 0.093     [W reducer.cpp:1251] Warning: find_unused_parameters=True was specified in DDP constructor, but did not find any unused parameters in the forward pass. This flag results in an extra traversal of the autograd graph every iteration,  which can adversely affect performance. If your model indeed never has any unused parameters in the forward pass, consider turning this flag off. Note that this warning may be a false positive if your model has flow control causing later iterations to have unused parameters. (function opEpoch 29  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98/98 0:02:53 • 0:00:00 0.75it/s loss: 0.0402 v_num: 0 val/acc:
                                                                          0.841 val/acc_best: 0.841     
Epoch 29  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98/98 0:02:53 • 0:00:00 0.75it/s loss: 0.0402 v_num: 0 val/acc:
                                                                          0.828 val/acc_best: 0.841     
                                                                          train/acc: 0.988            
                                                                          
Test stats:
Restoring states from the checkpoint path at /home/ubuntu/emlo-lightning-hydra-template/logs/train/cifar10/runs/2022-10-26_14-54-09/checkpoints/last.ckpt
Loaded model weights from checkpoint at /home/ubuntu/emlo-lightning-hydra-template/logs/train/cifar10/runs/2022-10-26_14-54-09/checkpoints/last.ckpt
Testing DataLoader 0: 100%|█████████████████████████████████████████████| 40/40 [06:46<00:00, 10.15s/it]
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Test metric        ┃       DataLoader 0        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│         test/acc          │    0.8331000208854675     │
│         test/loss         │    0.7881848216056824     │
└───────────────────────────┴───────────────────────────┘

S3 model checkpoint: [s3://emlo-session6-distributedtraining/last_ddp.ckpt](https://emlo-session6-distributedtraining.s3.amazonaws.com/last_ddp.ckpt)

