FROM python:3.10

ADD main.py .
ADD elements.json .
ADD dict.json .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]