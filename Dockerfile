FROM python:3

WORKDIR /chapter_2 


COPY requirements.txt .
COPY src/ .
RUN pwd
RUN ls

RUN pip install -r requirements.txt


# Run script.py when the container launches
CMD [ "python", "./src-temp-docker/ejemplo_101.py" ]
