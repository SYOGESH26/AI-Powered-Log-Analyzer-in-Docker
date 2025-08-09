import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

# Load logs from Phase 1
df = pd.read_csv("app_logs.csv")

df['message_len'] = df['message'].apply(len)
df['log_level'] = df['level'].map({'INFO': 0, 'WARNING': 1, 'ERROR': 2})
df['word_count'] = df['message'].apply(lambda x: len(x.split()))

X = df[['message_len', 'log_level', 'word_count']]

predictions = model.predict(X)

print("🚨 Detected Anomalies:")
print(df[predictions == 1])

