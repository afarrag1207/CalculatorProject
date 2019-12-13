FROM python:3.6

COPY . /web
WORKDIR /web
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python"]
CMD ["/web/Flask/app.py"]