💳 UPI Fraud Detection System
This project is a web-based fraud detection system that uses machine learning to identify fraudulent UPI transactions. Built using Streamlit for the frontend and optionally extendable with FastAPI for backend APIs, it leverages real-world financial transaction data to detect anomalies and prevent fraud.

🔗 Live Deployment
🚀 Hosted on: https://upi-fraud-9xve3mwccybqvrjpa86nzh.streamlit.app

🔗 GitHub Repository
📂 Code: https://github.com/Roopun/UPI-Fraud

🧠 Features
✅ Fraud Prediction based on:

PCA components of transaction data (V1–V28)

Transaction Time

Transaction Amount

✅ Streamlit-based Interactive Dashboard

User inputs for Time, Amount, and PCA features

Live prediction output

Easy to use and visually intuitive

✅ Machine Learning Backend

Trained model using Random Forest Classifier

Handles highly imbalanced datasets (only 492 frauds out of 284,807)

Scaled using StandardScaler

🗂️ Project Structure
bash
Copy
Edit
upi-fraud-detection/
│
├── model/                  
│   └── rf_model.pkl              # Trained Random Forest Classifier
│
├── streamlit_app/
│   ├── app.py                    # Streamlit frontend
│   └── requirements.txt
│
├── dataset/
│   └── creditcard.csv            # Dataset used for training and testing
│
├── UPI_Fraud_Detection.ipynb     # Jupyter notebook for model building
├── README.md                     # Project documentation
└── .gitignore
🛠️ How to Run Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Roopun/UPI-Fraud.git
cd UPI-Fraud
2. Install Dependencies
bash
Copy
Edit
pip install -r streamlit_app/requirements.txt
3. Run the Streamlit App
bash
Copy
Edit
streamlit run streamlit_app/app.py
📊 ML Model Details
✅ Random Forest Classifier
Input Features:

V1 to V28 (PCA components)

Time

Amount

Preprocessing:

Handled imbalanced data using class weights

Feature scaling using StandardScaler

Accuracy: ~99.9% (on test set)

Precision for Fraud Class: Very high, suitable for imbalanced binary classification.

🔐 Dataset Details
Source: Kaggle Credit Card Fraud Detection

Total Records: 284,807 transactions

Fraudulent Transactions: 492 (highly imbalanced)

All Features: PCA-anonymized components (V1–V28), Time, Amount, Class

🚀 Future Enhancements
Integrate FastAPI for scalable backend API

Include Email/SMS alerts on fraud detection

Add database logging for user inputs and results

Build an admin dashboard to track detection history

🙋‍♂️ Author
Snigdhendu Chattopadhyay
🔗 Live App
🔗 GitHub Repo
