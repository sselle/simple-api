FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apk add linux-headers
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "/usr/src/app/simple-api/api.py"]