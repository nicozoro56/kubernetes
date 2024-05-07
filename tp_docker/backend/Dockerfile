FROM python:3.10.14-alpine3.19
ENV PYTHONUNBUFFERED=1

VOLUME /tmp

COPY . /app

WORKDIR /app/src

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "main.py"]