# model_training.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Step 1: Load data
df = pd.read_csv("creditcard.csv")

# Step 2: Extract only necessary features
df = df[['Time', 'Amount', 'Class']]

# Step 3: Save known legit and fraud pairs for rule-based matching
df[['Time', 'Amount', 'Class']].to_csv("known_transactions.csv", index=False)

# Step 4: Scale 'Amount' and 'Time'
amount_scaler = StandardScaler()
time_scaler = StandardScaler()
df['scaled_amount'] = amount_scaler.fit_transform(df[['Amount']])
df['scaled_time'] = time_scaler.fit_transform(df[['Time']])

# Save scalers
joblib.dump(amount_scaler, "amount_scaler.pkl")
joblib.dump(time_scaler, "time_scaler.pkl")

# Step 5: Prepare features and target
X = df[['scaled_amount', 'scaled_time']]
y = df['Class']

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# Step 7: Handle imbalance
fraud_ratio = (y == 0).sum() / (y == 1).sum()

# Step 8: Train XGBoost model
model = XGBClassifier(
    scale_pos_weight=fraud_ratio,
    random_state=42,
    use_label_encoder=False,
    eval_metric='logloss'
)
model.fit(X_train, y_train)

# Step 9: Evaluate
y_pred = model.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 10: Save model
joblib.dump(model, "xgb_fraud_model.pkl")

print("✅ Model, scalers, and known transaction data saved.")
