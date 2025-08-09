import time
import pandas as pd
import random

levels = ["INFO", "WARNING", "ERROR"]

messages_info = [
    "User login successful",
    "Page loaded successfully",
    "File uploaded",
    "Cache refreshed",
    "Session started"
]

messages_error = [
    "Database connection failed",
    "Payment gateway timeout",
    "Null pointer exception",
    "Disk read error",
    "Login from unknown IP 222.111.45.67"
]

# Keep generating logs
logs = []
for i in range(30):
    if random.random() < 0.7:
        # Normal log
        logs.append({
            "timestamp": pd.Timestamp.now(),
            "level": "INFO",
            "message": random.choice(messages_info)
        })
    else:
        # Error log
        logs.append({
            "timestamp": pd.Timestamp.now(),
            "level": random.choice(["ERROR", "WARNING"]),
            "message": random.choice(messages_error)
        })

# Save logs to file
df = pd.DataFrame(logs)
df.to_csv("app_logs.csv", index=False)
print("📄 Logs generated at app_logs.csv")

