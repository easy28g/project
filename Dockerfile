FROM python:3
WORKDIR /usr/bin/app
COPY . .
RUN pip install -r requirements.txt