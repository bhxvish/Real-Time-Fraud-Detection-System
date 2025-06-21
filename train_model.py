import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("paysim.csv")

df = df[df['type'].isin(['TRANSFER','CASH_OUT'])]
df['type'] = df['type'].map({'TRANSFER':0, 'CASH_OUT': 1})
features = ['type','amount','oldbalanceOrg','oldbalanceDest']
x = df[features]
y = df['isFraud']
x_train, X_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators = 100, random_state = 42)
model.fit(x_train, y_train)
joblib.dump(model, "model.pkl")
