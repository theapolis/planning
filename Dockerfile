FROM python:3-alpine
COPY app.py /app/app.py
WORKDIR /app
RUN pip install Flask==1.0.2
ENTRYPOINT ["python"]
CMD ["app.py"]
