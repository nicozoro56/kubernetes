FROM python:3.10.14-alpine3.19

VOLUME /tmp

RUN rm -rf /app
COPY . /app

WORKDIR /app/src

RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["python3", "main.py"]