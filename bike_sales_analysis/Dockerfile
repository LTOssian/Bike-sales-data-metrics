FROM python:3.11-slim

RUN apt-get update && apt-get install -y postgresql-client

COPY ./batch/process_data.py .

CMD [ "python",  "process_data.py" ]