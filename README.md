# Real-Time Fraud Detection System

Detect fraudulent mobile money transactions in real time using machine learning. This project uses a **Random Forest classifier** trained on the **PaySim synthetic dataset**, mimicking real-world financial transaction patterns.

---

## Features

- Real-time prediction of fraudulent transactions  
- Trained on realistic transaction types (TRANSFER & CASH_OUT)  
- High precision Random Forest model  
- User-friendly UI for entering transaction details  
- Easily extensible with SHAP explainability or dashboards  
- Optional: Deployable on Streamlit Cloud or Hugging Face Spaces

---

## Dataset

We use the **Synthetic Financial Datasets For Fraud Detection**  
[Kaggle Link](https://www.kaggle.com/datasets/ealaxi/paysim1)

This dataset includes fields like:
- `type`: Transaction type (e.g., TRANSFER, CASH_OUT)
- `amount`: Transaction amount
- `oldbalanceOrg`: Sender's balance before transaction
- `oldbalanceDest`: Receiver's balance before transaction
- `isFraud`: Fraud label (1 for fraud, 0 for legit)

---

## How It Works

1. Filtered dataset to focus on `TRANSFER` and `CASH_OUT` types.
2. Trained a Random Forest model to predict `isFraud`.
3. Built a **Streamlit app** for real-time prediction based on:
   - Transaction type
   - Amount
   - Sender’s previous balance
   - Receiver’s previous balance

---

## Sample Inputs

| Type      | Amount  | Sender Balance | Receiver Balance | Prediction |
|-----------|---------|----------------|------------------|------------|
| TRANSFER  | 1000    | 5000           | 2000             |    Legit   |
| TRANSFER  | 100000  | 100000         | 0                |    Fraud   |
| CASH_OUT  | 20000   | 20000          | 0                |    Fraud   |
| CASH_OUT  | 2500    | 10000          | 5000             |    Legit   |

---

## Screenshots

### Safe transaction
<p align="center">
  <img src="safe output.png" width="700" alt="Safe">
</p>

### Fraud transaction
<p align="center">
  <img src="fraud output.png" width="700" alt="Fraud">
</p>

---

## Future Enhancements

- Add SHAP explainability for transparency  
- Visualize fraud stats over time  
- Add authentication layer for enterprise use  
- Deploy to cloud platform  

---

## Target Audience

This project is ideal for:
- Fintech/Banking interns
- Machine learning engineers
- Data science learners
- Hackathon participants

---

## Credits

Created by **Bhavish**  
Special thanks to the [PaySim team](https://www.kaggle.com/datasets/ealaxi/paysim1)

