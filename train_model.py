import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# 1. Load the dataset
# Ensure your CSV has a column named 'url' (or whatever your raw URL column is called)
# and a column named 'result' or 'target' for the labels (1 for phishing, 0 for safe)
data = pd.read_csv("phishing.csv")

# 2. Replicate the Flask Feature Extraction over the entire dataset
df_features = pd.DataFrame()
df_features['length'] = data['url'].apply(lambda x: len(str(x)))
df_features['dots'] = data['url'].apply(lambda x: str(x).count('.'))
df_features['http_clause'] = data['url'].apply(lambda x: int("https" in str(x)))
df_features['login_clause'] = data['url'].apply(lambda x: int("login" in str(x).lower()))

# 3. Define X and y using the engineered features
X = df_features
y = data['result'] # Make sure this matches your dataset's label column name

# 4. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Initialize and train the Random Forest Classifier
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# 6. Evaluate your model professionally (A must-have for your B.Tech report)
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

y_pred = model.predict(X_test)
print("\nDetailed Performance Report:")
print(classification_report(y_test, y_pred))

# 7. Save the model with the EXACT name used in your app.py
joblib.dump(model, "phishing_model.pkl")
print("\nSuccess: 'phishing_model.pkl' has been generated and is ready for Flask!")