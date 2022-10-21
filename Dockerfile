FROM python:3.8.14-slim-bullseye 

WORKDIR /app

COPY requirements.txt requirements.txt

COPY model.script.pt model.script.pt

RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . .

RUN rm -rf logs

CMD ["python", "src/demo_scripted.py", "ckpt_path=model.script.pt"]
