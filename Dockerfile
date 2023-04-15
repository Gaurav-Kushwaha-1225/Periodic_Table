FROM python:3.10

RUN pip install kivy kivymd

COPY ./*.py /app/
COPY ./*.json /app/
COPY ./*.ttf /app/

WORKDIR /app

CMD [ "python", "main.py" ]
