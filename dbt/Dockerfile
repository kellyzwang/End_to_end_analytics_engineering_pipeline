FROM python:3.11-slim

WORKDIR /usr/app

RUN pip install --no-cache-dir \
    "protobuf<5" \
    dbt-core==1.7.9 \
    dbt-mysql==1.7.0

CMD ["bash"]