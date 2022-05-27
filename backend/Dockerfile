FROM python:3.9.7

RUN apt update \
    && apt install -y default-mysql-client \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

ADD requirements.txt .

RUN pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt

ENV PORT 8080

WORKDIR /usr/src

COPY ./app /usr/src

CMD [ "python", "index.py" ]