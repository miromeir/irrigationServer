FROM python:3.8-alpine
RUN mkdir -p /app/server
COPY ./requirements.txt /app/server/requirements.txt
WORKDIR /app/server
RUN pip install -r requirements.txt
COPY . /app/server/
CMD ["FLASK_APP=main", "flask","run", "--host", "0.0.0.0"]