FROM python:3.11-slim
WORKDIR /web
COPY . .
EXPOSE 5000
RUN pip install flask flask_restx
EXPOSE 5000
CMD python app.py -b 0.0.0.0 app:app
