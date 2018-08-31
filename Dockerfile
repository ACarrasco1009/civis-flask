FROM continuumio/miniconda3:latest

LABEL maintainer="Alec Carrasco"

RUN pip install flask

COPY src /src/

EXPOSE 3838

ENTRYPOINT ["python", "/src/app.py"]