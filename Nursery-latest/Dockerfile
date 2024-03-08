FROM python:3.9.16

RUN pip install django==4.2.11
COPY . .

RUN pip install -r requirements.txt
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

































