FROM python:3.10-slim-bullseye 
ADD app.py /
ADD templates/ /templates
ADD static/ /static
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD [ "python", "./app.py" ]
