FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]

# Install gRPC tools
