FROM python:3

ADD . .

RUN pip install --upgrade pip

CMD ["python", "-m", "unites", "discover", "-s","Tests"]
