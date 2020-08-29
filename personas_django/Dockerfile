FROM python:3.8.5

COPY sap /sap

COPY requirements.txt /sap/requirements.txt

WORKDIR /sap

RUN pip install -r requirements.txt && chmod 755 /sap/manage.py

CMD python manage.py runserver 0.0.0.0:8000
