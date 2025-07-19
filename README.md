# 💳 UPI Fraud Detection System

This project is a web-based fraud detection system that uses machine learning to identify fraudulent UPI transactions. Built using **Streamlit** for the frontend and optionally extendable with **FastAPI** for backend APIs, it leverages real-world financial transaction data to detect anomalies and prevent fraud.

🔗 **Live Deployment**  
🚀 Hosted on: [https://upi-fraud-9xve3mwccybqvrjpa86nzh.streamlit.app](https://upi-fraud-9xve3mwccybqvrjpa86nzh.streamlit.app)

🔗 **GitHub Repository**  
📂 Code: [https://github.com/Roopun/UPI-Fraud](https://github.com/Roopun/UPI-Fraud)

---

## 🧠 Features

✅ **Fraud Prediction based on:**
- PCA components of transaction data (V1–V28)
- Transaction Time
- Transaction Amount

✅ **Streamlit-based Interactive Dashboard**
- User inputs for Time, Amount, and PCA features
- Live prediction output
- Easy to use and visually intuitive

✅ **Machine Learning Backend**
- Trained model using `XGBoost Classifier`
- Handles highly imbalanced datasets (only 492 frauds out of 284,807)
- Scaled using `StandardScaler`

---

## 🗂️ Project Structure

📁 UPI-Fraud-Detection/
├── 📄 app.py               → Streamlit application script
├── 📄 requirements.txt     → Python dependencies
├── 📄 xgb_fraud_model.pkl  → Trained XGBoost fraud detection model
├── 📄 amount_scaler.pkl    → Scaler for the 'Amount' feature
├── 📄 time_scaler.pkl      → Scaler for the 'Time' feature
└── 📄 README.md            → Project overview and usage instructions
                # Project overview and setup instructions
