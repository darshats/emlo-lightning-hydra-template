FROM python:3.8.14-slim-bullseye 

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "src/train.py"]
