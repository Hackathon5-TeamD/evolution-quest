FROM python:3.9.7

RUN apt update \
    && apt install -y default-mysql-client \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

WORKDIR /usr/src/app/app

ENV FLASK_APP=app

COPY ./backend/flask_app/requirements.txt .
# COPY . .

RUN pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt

# COPY ./app /usr/src
  
CMD [ "uwsgi", "--ini", "/usr/src/app/app/uwsgi.ini" ]