# Order is attempting to optimize for cache hit
FROM python:3.8-alpine3.10
LABEL maintainer="Witt Allen @wittionary"
ADD requirements.txt /
RUN pip install -r requirements.txt
ARG API_KEY
ENV Maps_API_Key=${API_KEY}

ADD /templates/index.html /templates/index.html
ADD /static/js/button.js /static/js/button.js
ADD /static/css/index.css /static/css/index.css

ADD app.py /
RUN chmod 644 app.py

EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]