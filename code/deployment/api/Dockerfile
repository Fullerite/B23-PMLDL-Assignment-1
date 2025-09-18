FROM python:3.11-slim

WORKDIR /app

COPY code/deployment/api/app.py /app/
COPY models/mpg_model.pkl /app/models/

RUN pip install fastapi uvicorn scikit-learn pandas

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
