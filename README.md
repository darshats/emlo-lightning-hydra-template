This is assignment 4 - dockerize the demo application.

In order to run the application outside docker, please clone the repo and run: python src/demo_scripted.py ckpt_path=model.script.pt
This should start the gradio server on default port 7860 which runs the cifar10 model that was trained for 10 epochs.

The second part of assignment isnt fully working. The image size is 3GB so its above the limit. The port 8080 is not being exposed from inside the docker image - not sure why. However if it were to work, the cmdline after pulling the docker image is docker run -t -p 8080:8080 demo:v1

Dockerhub link: https://hub.docker.com/layers/darshats/dockerhub/myfirstimagepush/images/sha256:bd954c1dcd2e6ef1ca092e47f53056a082084a3d9db671b4f05f1ca60ab302fb
docker pull darshats/dockerhub:myfirstimagepush
