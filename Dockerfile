# A sample run a Flask program
# Guide: https://blog.bitsrc.io/a-guide-to-docker-multi-stage-builds-206e8f31aeb8
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

EXPOSE 8080
CMD [ "python", "KAAS_Assignment/manage.py", "migrate"]
CMD [ "python", "KAAS_Assignment/manage.py", "runserver", "0.0.0.0:8000"]
