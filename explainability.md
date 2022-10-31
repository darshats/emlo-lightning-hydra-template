
There are 10 images that are run through explain.py. The output of various algos is shown below. For the gradcam, the image tensor needs a permute between w & h axis. Sometimes this worked, sometimes it needed permute and I didnt figure out why it was happening.

1) Predicted tiger cat, (0.3682238757610321)
IG
![image](https://user-images.githubusercontent.com/56063876/199012694-d18d775f-e884-4d3b-a485-b58227ef957f.png)

IG /w NT
![image](https://user-images.githubusercontent.com/56063876/199012776-70a264a0-a56f-4661-86ba-caeaea0542f9.png)

Shap gradient
![image](https://user-images.githubusercontent.com/56063876/199012838-27067e29-e581-416f-a3ff-42551d9cbadf.png)

Occlusion
![image](https://user-images.githubusercontent.com/56063876/199012897-5c1d5385-d193-4ba2-8135-9016254bc2cc.png)

Shap
![image](https://user-images.githubusercontent.com/56063876/199012987-6ac16257-941b-4e25-9fa4-c1fc9e6410fb.png)

GadCAM
![image](https://user-images.githubusercontent.com/56063876/199013021-66d6f7ee-4bb1-4d33-8a62-ac27b750b51b.png)

GradCAM++
![image](https://user-images.githubusercontent.com/56063876/199013058-fff389fc-1f49-49ca-b685-71b087be643e.png)

