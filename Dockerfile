<<<<<<< HEAD
FROM python:3.8.4
=======
FROM python:3
>>>>>>> 552d4c350106bbe0a27c4ced3ebc402d6e53c48b
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY ./  /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
