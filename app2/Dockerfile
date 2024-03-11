FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8082 

ENTRYPOINT [ "python" ]

CMD [ "app2.py" ]

