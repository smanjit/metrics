FROM python:latest
COPY src/. /app
COPY requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /app
EXPOSE 5005
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
