
FROM python:3.10-slim-buster
EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt


#adding requirements
RUN pip3 install -r requirements.txt

COPY . .


CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]