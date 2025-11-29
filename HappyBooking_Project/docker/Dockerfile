FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    numpy==1.24.3 \
    pandas==2.0.3 \
    azure-eventhub==5.11.5

COPY stream_producer.py /app/
COPY hotel_raw_stream.csv /app/

ENV CSV_FILE=hotel_raw_stream.csv
ENV DELAY_SECONDS=0
ENV BATCH_SIZE=1000

CMD ["python", "stream_producer.py"]