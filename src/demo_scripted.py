import pyrootutils
import numpy as np

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

from typing import List, Tuple

import torch
import torchvision
import hydra
import gradio as gr
from omegaconf import DictConfig
import requests

from src import utils

log = utils.get_pylogger(__name__)

def demo(cfg: DictConfig) -> Tuple[dict, dict]:
    """Demo function.
    Args:
        cfg (DictConfig): Configuration composed by Hydra.

    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    assert cfg.ckpt_path

    log.info("Running Demo")

    log.info(f"Instantiating scripted model <{cfg.ckpt_path}>")
    model = torch.jit.load(cfg.ckpt_path)
    # ckpt = torch.load('/home/dshah/emlo-lightning-hydra-template/logs/train/cifar10/runs/2022-10-21_14-28-50/checkpoints/epoch_009.ckpt')
    # model: LightningModule = hydra.utils.instantiate(cfg.model)
    # model.load_state_dict(ckpt["state_dict"])
    model.eval()
    # log.info(f"Loaded Model: {model}")

    labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    def recognize_cifar10(image):
        if image is None:
            return None
        image = np.transpose(np.array(image), (2, 0, 1))
        image_t = torch.tensor(image, dtype=torch.float32)
        image_t = torchvision.transforms.Resize(size=(32,32))(image_t).unsqueeze(0)
        print(image_t.size())
        preds = model.forward_jit(image_t)
        # preds = model(image_t)
        preds = preds[0].tolist()
        return {labels[i]: preds[i] for i in range(10)}

    # im = gr.Image(shape=(28, 28), image_mode="L", invert_colors=True, source="canvas")

    demo = gr.Interface(
        fn=recognize_cifar10,
        inputs=gr.Image(type="pil"),
        outputs=[gr.Label(num_top_classes=10)],
        live=True,
    )

    log.info(f'launching demo on port 8080!')
    demo.launch(server_port=8080)
    

@hydra.main(
    version_base="1.2", config_path=root / "configs", config_name="demo_scripted.yaml"
)
def main(cfg: DictConfig) -> None:
    demo(cfg)

if __name__ == "__main__":
    main()