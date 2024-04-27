FROM python:3.8-slim

WORKDIR /

COPY . /

RUN pip install --no-cache-dir -r requirements.txt

# REQUIRE ENV variables on runtime
#DB_USER
#DB_PASS
#DB_HOST
#DB_PORT
#DB_NAME

EXPOSE 8082

CMD ["python", "run.py"]

