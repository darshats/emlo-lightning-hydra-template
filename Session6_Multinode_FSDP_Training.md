Below are details of multinode FSDP training for CIFAR10 and VIT224

GPU nodes: 2 
Type: G4dn.xlarge Strategy: DDP

Train stats: Batch size: 512 LR: 0.0001
Trainable params: 87.5 M                                                                                
Non-trainable params: 0                                                                                 
Total params: 87.5 M                                                                                    
Total estimated model params size (MB): 174                                                             
/opt/conda/envs/pytorch/lib/python3.9/site-packages/pytorch_lightning/trainer/trainer.py:1894: 
PossibleUserWarning: The number of training batches (44) is smaller than the logging interval 
Trainer(log_every_n_steps=50). Set a lower value for log_every_n_steps if you want to see logs for the 
training epoch.
  rank_zero_warn(
Epoch 29  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49/49 0:00:51 • 0:00:00 1.02it/s loss: 0.00255 v_num: 0        
                                                                          val/acc: 0.971 val/acc_best:  
Epoch 29  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49/49 0:00:51 • 0:00:00 1.02it/s loss: 0.00255 v_num: 0        
                                                                          val/acc: 0.976 val/acc_best:  
                                                                          0.98 train/acc: 0.999         
                                                                          
Test stats:
Restoring states from the checkpoint path at /home/ubuntu/emlo-lightning-hydra-template/logs/train/cifar10/runs/2022-10-26_17-51-58/checkpoints/last.ckpt
Loaded model weights from checkpoint at /home/ubuntu/emlo-lightning-hydra-template/logs/train/cifar10/runs/2022-10-26_17-51-58/checkpoints/last.ckpt
Testing DataLoader 0: 100%|█████████████████████████████████████████████| 40/40 [08:11<00:00, 12.29s/it]
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Test metric        ┃       DataLoader 0        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│         test/acc          │    0.9789999723434448     │
│         test/loss         │    0.09007707238197327    │
└───────────────────────────┴───────────────────────────┘

S3 bucket endpoint: https://emlo-session6-distributedtraining.s3.amazonaws.com/last_fsdp.ckpt
