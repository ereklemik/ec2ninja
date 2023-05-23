FROM  python:3.9
WORKDIR /mid/flask_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY flask_app/app.py .
COPY flask_app/templates ./templates
EXPOSE 5000
CMD ["python", "app.py"]
