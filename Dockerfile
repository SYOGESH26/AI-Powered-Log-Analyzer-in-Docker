FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install pandas scikit-learn pyod joblib
CMD ["sh", "-c", "python train_model.py && python detect_anomalies.py"]

