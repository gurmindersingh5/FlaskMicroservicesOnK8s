FROM python:3.8-slim

WORKDIR /

COPY . /

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

CMD ["python", "run.py"]

