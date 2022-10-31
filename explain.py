import timm
import torch
import urllib
import requests
import torchvision.transforms as T
import torch.nn.functional as F
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

from captum.attr import IntegratedGradients, NoiseTunnel, visualization as viz
from captum.attr import GradientShap, Occlusion

import shap

from pytorch_grad_cam import GradCAM, HiResCAM, ScoreCAM, GradCAMPlusPlus, AblationCAM, XGradCAM, EigenCAM, FullGrad
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
from pytorch_grad_cam.utils.image import show_cam_on_image

def do_IG(img_tensor, transformed_img, pred_label_idx, model):
    integrated_gradients = IntegratedGradients(model)
    default_cmap = LinearSegmentedColormap.from_list('custom_blue',
                                                        [(0, '#ffffff'),
                                                         (0.25, '#00ff00'),
                                                         (1, '#000000')], N=256)

    attribution_ig = integrated_gradients.attribute(img_tensor, target=pred_label_idx, n_steps=100)


    _ = viz.visualize_image_attr(np.transpose(attribution_ig.squeeze().cpu().detach().numpy(), (1,2,0)),
                                 np.transpose(transformed_img.squeeze().cpu().detach().numpy(), (1,2,0)),
                                 method='heat_map',
                                 cmap = default_cmap,
                                 show_colorbar=True,
                                 sign='positive',
                                 outlier_perc=1)
    
## Noise Tunnel
def do_IG_NT(img_tensor, transformed_img, pred_label_idx, model):
    
    integrated_gradients = IntegratedGradients(model)
    noise_tunnel = NoiseTunnel(integrated_gradients)
    attributions_ig_nt = noise_tunnel.attribute(img_tensor, target=pred_label_idx, 
                                                nt_samples=10, nt_type='smoothgrad_sq')
    _ = viz.visualize_image_attr(np.transpose(attributions_ig_nt.squeeze().cpu().detach().numpy(), (1,2,0)),
                                 np.transpose(transformed_img.squeeze().cpu().detach().numpy(), (1,2,0)),
                                 'heat_map',
    #                              ['all', 'positive'],
                                 'positive',
                                 cmap = default_cmap,
                                 show_colorbar=True)
    
    
## Gradient SHAP
def do_shap_gradient(img_tensor, transformed_img, pred_label_idx, model):
    gradient_shap = GradientShap(model)
    rand_img_dist = torch.cat([img_tensor*0, img_tensor*1])
    attributions_gs = gradient_shap.attribute(img_tensor, n_samples=50, stdevs=0.0001,
                                             baselines=rand_img_dist, target=pred_label_idx)
    _ = viz.visualize_image_attr(np.transpose(attributions_gs.squeeze().cpu().detach().numpy(), (1,2,0)),
                                 np.transpose(transformed_img.squeeze().cpu().detach().numpy(), (1,2,0)),
                                 'heat_map',
                                 'absolute_value',
                                 cmap = default_cmap,
                                 show_colorbar=True)
    
    
## Occlusion
def do_occlusion(img_tensor, transformed_img, pred_label_idx, model):
    occlusion = Occlusion(model)
    attributions_occ = occlusion.attribute(img_tensor, strides=(3,8,8), target=pred_label_idx, 
                                           sliding_window_shapes=(3,15,15), baselines=0)
    _ = viz.visualize_image_attr_multiple(np.transpose(attributions_occ.squeeze().cpu().detach().numpy(), (1,2,0)),
                                          np.transpose(transformed_img.squeeze().cpu().detach().numpy(), (1,2,0)),
                                          ['original_image', 'heat_map'],
                                          ['all', 'positive'],
                                          cmap = default_cmap,
                                          show_colorbar=True,
                                          outlier_perc=2)
    
    
## SHAP
def do_shap(img_tensor, transformed_img, pred_label_idx, model):
    inv_transform = T.Compose([
        T.Lambda(lambda x: x.permute(0,3,1,2)),
        T.Normalize(
            mean = (-1 * np.array(mean) / np.array(std)).tolist(),
            std = (1 / np.array(std)).tolist()
        ),
        T.Lambda(lambda x: x.permute(0,2,3,1)),
    ])


    def predict(imgs: torch.Tensor):
        imgs = torch.tensor(imgs)
        imgs = imgs.permute(0,3,1,2)

        img_tensor = imgs.to(device)
        output = model(img_tensor)
        return output

    topk=4
    batch_size=50
    n_evals=10000

    masker_blur = shap.maskers.Image("blur(128,128)", (224,224,3))
    explainer = shap.Explainer(predict, masker_blur, output_names=categories)

    img_tensor1 = transformed_img.unsqueeze(0)
    img_tensor1 = img_tensor1.permute(0,2,3,1)

    shap_values = explainer(img_tensor1, max_evals=n_evals, batch_size=batch_size,
                            outputs = shap.Explanation.argsort.flip[:topk])

    shap_values.data = inv_transform(shap_values.data).cpu().numpy()[0]
    shap_values.values = [val for val in np.moveaxis(shap_values.values[0], -1, 0)]

    shap.image_plot(shap_values=shap_values.values,
                    pixel_values=shap_values.data,
                    labels=shap_values.output_names,
                    true_labels=[categories[285]])
    
    
def do_gradcam(img_tensor, transformed_img, pred_label_idx, model):
    
    target_layers = [model.layer4[-1]]
    cam = GradCAM(model=model, target_layers=target_layers, use_cuda=True)
    targets = [ClassifierOutputTarget(285)]
    grayscale_cam = cam(input_tensor=transformed_img.unsqueeze(0), targets=targets)
    grayscale_cam = grayscale_cam[0,:]
    rgb_img = transformed_img.cpu().squeeze().permute(2,1,0).detach().numpy()
    visualization = show_cam_on_image(rgb_img, grayscale_cam, use_rgb=True)
    
    plt.imshow(visualization)
    plt.show()
    
    
    
def do_gradcamplusplus(img_tensor, transformed_img, pred_label_idx, model):
    target_layers = [model.layer4[-1]]
    cam = GradCAMPlusPlus(model=model, target_layers=target_layers, use_cuda=True)
    targets = [ClassifierOutputTarget(285)]
    grayscale_cam = cam(input_tensor=transformed_img.unsqueeze(0), targets=targets)
    grayscale_cam = grayscale_cam[0,:]
    rgb_img = transformed_img.cpu().squeeze().permute(2,1,0).detach().numpy()
    visualization = show_cam_on_image(rgb_img, grayscale_cam, use_rgb=True)
    
    plt.imshow(visualization)

device = torch.device('cuda')
model = timm.create_model('resnet18', pretrained=True)
model.eval()
model = model.to(device)

mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]

# Download human-readable labels for ImageNet.
response = requests.get("https://git.io/JJkYN")
categories = response.text.split("\n")

transform = T.Compose([T.Resize((224, 224)), T.ToTensor()])
transform_normalize = T.Normalize(
    mean=mean, std=std
)

for imgfile in ['Cat03.jpg', 'ambulance.jpg', 'balloon.jpg',
                'bee.jpg', 'camel.jpg', 'cannon.jpg', 'hen.jpg',
                'macaw.jpg', 'tiger.jpg', 'zebra.jpg']:
    img = Image.open(imgfile)
    transformed_img = transform(img)
    img_tensor = transform_normalize(transformed_img)
    img_tensor = img_tensor.unsqueeze(0).to(device)
    print(f'min {torch.min(img_tensor)}, max {torch.max(img_tensor)}')
    output = model(img_tensor)
    output = F.softmax(output, dim=1)
    prediction_score, pred_label_idx = torch.topk(output, 1)
    pred_label_idx.squeeze_()
    predicted_label = categories[pred_label_idx.item()]
    print(f'Predicted {predicted_label}, ({prediction_score.squeeze().item()})')
    
    print(f'IG')
    do_IG(img_tensor, transformed_img, pred_label_idx, model)
    print(f'IG /w Noise tunnel')
    do_IG_NT(img_tensor, transformed_img, pred_label_idx, model)
    print(f'Shap gradient')
    do_shap_gradient(img_tensor, transformed_img, pred_label_idx, model)
    print(f'Occlusion')
    do_occlusion(img_tensor, transformed_img, pred_label_idx, model)
    print('Shap')
    do_shap(img_tensor, transformed_img, pred_label_idx, model)
    print(f'GradCAM')
    do_gradcam(img_tensor, transformed_img, pred_label_idx, model)
    print(f'GradCAM++')
    do_gradcamplusplus(img_tensor, transformed_img, pred_label_idx, model)

