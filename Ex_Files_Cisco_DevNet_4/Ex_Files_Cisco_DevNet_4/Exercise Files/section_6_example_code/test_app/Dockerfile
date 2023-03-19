FROM python:alpine3.7
WORKDIR /home/ubuntu
RUN mkdir /home/ubuntu/app
COPY app.py /home/ubuntu/app
RUN pip install flask
CMD python /home/ubuntu/app/app.py
EXPOSE 8080
