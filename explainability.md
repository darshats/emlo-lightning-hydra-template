
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

2) Predicted ambulance, (0.8612079620361328)
IG ![image](https://user-images.githubusercontent.com/56063876/199013637-5b458f4c-ad1e-4dd6-8a10-3365f1a76bc8.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199013691-cfc93e56-6c01-4dd5-9e12-d15a09703c50.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199013734-791184c8-60ae-4d13-9e9a-8a7e8336fd59.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199013782-30db5959-51d2-457a-b0ee-f0b3bfd70bf4.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199013815-b279735a-2233-4d74-a043-13be661e4abd.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199013861-7071a151-604c-44c7-8fe7-8fa9478c2097.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199013896-76fe8f27-bd84-4278-8975-84ebf605de08.png)


3) Predicted punching bag, (0.6095880270004272). Actually this was balloon.
IG ![image](https://user-images.githubusercontent.com/56063876/199014008-a4b524ca-c19d-4bad-a5a6-47c95b2ce487.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199014043-3964edad-fde6-458c-b77c-a37353d9062b.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199014095-5362959c-192c-4853-b64a-292a3451a10e.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199014128-64c6bdf7-0700-41e1-bc72-2293c55ac4f2.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199014177-2a965949-1f8a-4c78-ba4a-6d6af1102a8f.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199014221-0822b3a2-010c-48f4-9a16-668fa0bae1f6.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199014254-21b38226-06f8-4d4f-9f9a-6b91d8add17a.png)


4) Predicted bee, (0.9759519100189209)
IG ![image](https://user-images.githubusercontent.com/56063876/199014340-65e8a3c4-be13-4db7-991c-229c92c0c5ad.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199014374-c3e4bf9c-63fc-4c9f-ad40-1b1d93e4b6b9.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199014414-96132f63-1848-4245-85d8-28c297db2bc1.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199014435-0e6b5fe5-8998-4588-ae81-5536fb89c392.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199014490-e1763056-9474-4cd3-a010-0dcd0b95a743.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199014528-4e24ae6d-1f34-4c90-9c93-584c5823909b.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199014581-a17d55d8-289e-4402-8370-62c4c052182c.png)

5) Predicted Arabian camel, (0.9995625615119934)
IG ![image](https://user-images.githubusercontent.com/56063876/199014672-269a4c8d-4f53-4dde-8e34-2c318c878c54.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199014713-1348cda5-08d0-4867-a438-38bd1cbfc2ef.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199014795-6ab66e8c-0613-4c62-bbd8-e19999171e02.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199014845-76128cf0-afa2-4e5d-8307-44b09ec0d151.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199014872-143e5328-0cc4-45c4-b202-9c367432aaff.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199014908-0b6c54c6-7ad0-4ce1-8fe1-17a36cd34b96.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199014938-52a56401-2dc5-4ada-9121-2cec14dd39f2.png)

6) 

