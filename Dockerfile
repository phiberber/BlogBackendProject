FROM python:3.6

WORKDIR /package

COPY requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt