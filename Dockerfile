FROM python:3.11-slim
WORKDIR /web
COPY . .
EXPOSE 5000
RUN pip install flask flask_restx
CMD python app.py
