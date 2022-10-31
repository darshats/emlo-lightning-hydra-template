
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



6) Predicted cannon, (0.7962093949317932)
IG ![image](https://user-images.githubusercontent.com/56063876/199015152-5c906170-9ed2-497a-a927-95c9ae745ad6.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199015200-10d7b8ab-7dac-447d-939d-8b23196902d7.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199015262-e612f728-518f-4ad6-81c5-40c54ae1f03e.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199015299-00fd7b9c-844b-4485-848d-ac7945e90e33.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199015328-39afa150-5c0e-4818-9e55-2fc2f2db21e1.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199015361-914b5e2b-8de8-4843-9450-805c8bb69dd6.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199015405-631ca0ae-3b0c-4323-9a2a-e2b9d46649cf.png)


7) Predicted hen, (0.8744664788246155)
IG ![image](https://user-images.githubusercontent.com/56063876/199015504-727f6c8d-96a9-472a-9cf0-48068c1532ca.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199015535-9095f1c8-e006-42a6-a115-e898fa2a7aa8.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199015578-1c704dae-df10-42c8-9e31-fb8127ef8ea5.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199015602-9c08bcd7-200a-45bb-81e5-05d9e11887a4.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199015645-48257272-2226-43e9-a709-025fe36ffa9c.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199015678-091288b0-0c61-4a39-bd66-8efa57aa2aa2.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199015711-b70e0aa4-3254-423a-b145-df9e5445cd5b.png)


8) Predicted macaw, (0.9977763295173645)
IG ![image](https://user-images.githubusercontent.com/56063876/199015797-09794a40-60fa-4491-ba63-0b89fe109945.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199015835-356e866d-e377-40a2-b9d0-95ff3412bdf7.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199015883-5482a33a-1ac2-4d03-ac9a-2ad45e6d11ef.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199015946-183cd464-f163-4ce2-bfe9-4abb0d816658.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199015980-956ea62e-3cfb-4d65-890b-a4039f41ea55.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199016026-d7524ba9-c93a-4e5a-89ab-d38151fd1eda.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199016065-8dec77b7-4d9f-4675-aca2-ba312c730c25.png)


9) Predicted tiger, (0.6982722878456116)
IG ![image](https://user-images.githubusercontent.com/56063876/199016140-866f3200-00dc-49b7-9822-84aebcfc9caf.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199016176-a7a08fac-aa3c-40e0-a600-9ba508cc7586.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199016205-9d0353d3-4ef6-49a7-9949-3b651c1d0927.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199016229-032c59c4-37bb-45b3-8136-92a2616cc2c7.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199016277-b6fd1a8c-15e8-41e8-8675-1e24169dd981.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199016317-7832d0fc-779d-46a2-bece-3c105fca8b15.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199016346-25558580-9101-42cd-948f-5f08fec365ad.png)


10) Predicted zebra, (0.9988380074501038)
IG ![image](https://user-images.githubusercontent.com/56063876/199016413-43a8dff6-a1a6-4c52-a254-c3a8814fbd18.png)

IG /w NT ![image](https://user-images.githubusercontent.com/56063876/199016444-1ae44d00-c690-4d44-ac48-b90c0762075f.png)

Shap gradient ![image](https://user-images.githubusercontent.com/56063876/199016489-2b451130-64bf-4356-b3cf-540a60d8cfbe.png)

Occlusion ![image](https://user-images.githubusercontent.com/56063876/199016527-32fb6d99-ccf0-40db-8d37-74bde7f48389.png)

Shap ![image](https://user-images.githubusercontent.com/56063876/199016566-448526a1-5c0e-44b6-adca-015db3d0d514.png)

GradCAM ![image](https://user-images.githubusercontent.com/56063876/199016594-a66bd0e4-3062-459b-8d5f-419c8d9c365a.png)

GradCAM++ ![image](https://user-images.githubusercontent.com/56063876/199016628-f9786183-2abe-4117-a8b0-4d4f80d0568f.png)


