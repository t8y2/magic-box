FROM python:3.11-bookworm
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple --no-cache-dir
CMD ["python","main.py"]
EXPOSE 6537
