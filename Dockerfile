FROM python:3-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app/


RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

RUN python3 manage.py migrate

EXPOSE 8000

CMD [ "python3", "-m", "gunicorn", "task_management_system.wsgi", "-w", "4", "--bind", "0.0.0.0:8000" ]