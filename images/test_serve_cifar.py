import requests
import os

for image in os.listdir():
    response = requests.put(f'http://127.0.0.1:8080/predictions/cifar10 {image}')
    if response.status_code == 200:
        d = dict(response.text)
        for k, v in d.items():
            print(k, v)
            break
