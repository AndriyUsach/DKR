FROM python:3.8

ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY . /src/

COPY requirements.txt .
RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]