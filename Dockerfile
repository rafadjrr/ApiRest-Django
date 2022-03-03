FROM python:3.6

WORKDIR /usr/src/app

COPY requeriments.txt ./

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

CMD ["python", "./manage.py"]
