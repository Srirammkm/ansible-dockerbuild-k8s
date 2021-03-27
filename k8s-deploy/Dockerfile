FROM python:3
USER root
COPY . /app/
WORKDIR /app/
RUN pip install flask
RUN pip install mysql-connector-python
EXPOSE 80
CMD [ "python","app.py"]
