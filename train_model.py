import pandas as pd
from pyod.models.iforest import IForest
import joblib

# Train only on normal logs
logs = [
    {"timestamp": "2025-08-09 12:00:01", "level": "INFO", "message": "User login successful"},
    {"timestamp": "2025-08-09 12:00:02", "level": "INFO", "message": "Page loaded successfully"},
    {"timestamp": "2025-08-09 12:00:03", "level": "INFO", "message": "File uploaded"},
    {"timestamp": "2025-08-09 12:00:04", "level": "INFO", "message": "Cache refreshed"}
]
df = pd.DataFrame(logs)

df['message_len'] = df['message'].apply(len)
df['log_level'] = df['level'].map({'INFO': 0, 'WARNING': 1, 'ERROR': 2})
df['word_count'] = df['message'].apply(lambda x: len(x.split()))

X = df[['message_len', 'log_level', 'word_count']]

model = IForest()
model.fit(X)

joblib.dump(model, 'model.pkl')
print("✅ Model trained and saved as model.pkl")

