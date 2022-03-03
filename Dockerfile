FROM registry.redhat.io/ubi8/python-36

WORKDIR /usr/src/app

EXPOSE 8080

COPY requeriments.txt ./

RUN pip install gunicorn

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

CMD ["python","manage.py","runserver","0:8080"]
