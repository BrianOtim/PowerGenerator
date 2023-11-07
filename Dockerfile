FROM python:alpine
COPY powergenerated.py /app/
WORKDIR /app
RUN pip install matplotlib
CMD ["python", "powergenerated.py"]
