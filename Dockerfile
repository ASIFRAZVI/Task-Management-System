FROM python:3-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app/

RUN pip install -r requirement.txt
RUN pip install gunicorn

# RUN python manage.py migrate

EXPOSE 8015

CMD [ "python3", "-m", "gunicorn", "task_management_system.wsgi:application", "-w", "4", "--bind", "0.0.0.0:8015" ]