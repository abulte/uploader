FROM python:3.7-slim
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
CMD ["flask", "run", "-h", "0.0.0.0"]
