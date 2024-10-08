FROM python:3.13-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["get_config.py", "main.py"]
