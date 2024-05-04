FROM python:3.11-slim
WORKDIR /web
COPY . .
EXPOSE 80
RUN pip install flask flask_restx
CMD python app.py -b 0.0.0.0 app:app
