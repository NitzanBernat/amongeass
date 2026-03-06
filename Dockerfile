FROM python:3.10-slim
WORKDIR /app
LABEL authors="Magshimim_AI"
COPY requirments.txt .


#install dependencies
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirments.txt


COPY . .
EXPOSE 8080
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080","top", "-b","python", "app.py"]