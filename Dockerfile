FROM python:3.9
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 80
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
