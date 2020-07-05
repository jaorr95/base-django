FROM python:3.8.3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY docker-entrypoint.py /

EXPOSE 80

ENTRYPOINT ["python", "/docker-entrypoint.py"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

