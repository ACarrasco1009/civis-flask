FROM continuumio/miniconda3:latest

LABEL maintainer="Alec Carrasco"

RUN pip install -r requirements.txt

COPY src /src/

EXPOSE 3838

ENTRYPOINT ["python", "/src/app.py"]