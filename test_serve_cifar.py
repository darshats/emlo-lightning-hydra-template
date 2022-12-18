import requests
import os
import json 

for image in os.listdir('./images'):
    response = requests.post('http://127.0.0.1:8080/predictions/cifar10',
                             files={'data': open(f'images/{image}', 'rb')}
                            )
    if response.status_code == 200:
        d = dict(json.loads(response.text))
        print(f'For image {image}')
        for k, v in d.items():
            print(f'\toutput {k}:{v}')
    else:
        print(f'Error with request: {response.status_code}')
