# Created by Kay Men Yap 19257442
# Last updated: 28/09/2020
# Purpose: To build the docker image for the program to run on
FROM python:3
LABEL Kay "19257442@student.curtin.edu.au"
ENV PYTHONUNBUFFERED 1

# Create app directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY src/requirements.txt .
# Install app dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

COPY src .
RUN python KAAS_Assignment/manage.py makemigrations
RUN python KAAS_Assignment/manage.py migrate

EXPOSE 8080
CMD [ "python", "KAAS_Assignment/manage.py", "runserver", "0.0.0.0:8000"]
