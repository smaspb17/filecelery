FROM python:3.10
RUN apt-get update -y
RUN apt-get upgrade -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "manage.py", "runserver", "0:8000"]