
FROM python:3.10-slim-buster
EXPOSE 5000

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]