FROM python:3.11-slim

WORKDIR /app

COPY code/deployment/app/streamlit_app.py /app/

RUN pip install streamlit requests

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py"]
