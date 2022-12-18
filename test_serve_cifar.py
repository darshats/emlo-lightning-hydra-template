import requests
import os

for image in os.listdir(images):
    response = requests.post('http://127.0.0.1:8080/predictions/cifar10',
                             files={'data': open(f'images/{image}', 'rb')}
                            )
    if response.status_code == 200:
        d = dict(response.text)
        for k, v in d.items():
            print(k, v)
    else:
        print(f'Error with request: {response.status_code}')