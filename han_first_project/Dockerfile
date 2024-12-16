# Pull the image from Dockerhub
FROM python:alpine3.21

WORKDIR /han_first_project

# set up python environment variables

ENV PYTHONDOWNWRITEBYTECODE 1
ENV PYTHONNUNBUFFER 1

# update and  install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /han_first_project/requirements.txt
RUN pip install -r /han_first_project/requirements.txt

# copy project
COPY . .

# Expose the port server is running on
EXPOSE 8000
