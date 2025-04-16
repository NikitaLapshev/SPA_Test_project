FROM python:3.12

ENV PYTHONUNDUFFERED=1

WORKDIR /code


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8000