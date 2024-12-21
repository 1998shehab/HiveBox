FROM python

WORKDIR /APP

COPY . /APP

CMD ["python", "APP.py"] 
