# Python 環境の指定
FROM python:3.7.3

WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /app

# CMD ["python", "app.py"]
