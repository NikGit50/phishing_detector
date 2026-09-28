from flask import Flask, render_template, request
import joblib
import mysql.connector
from urllib.parse import urlparse
import re

app = Flask(__name__)

# Load your model
model = joblib.load("phishing_model.pkl")

# MySQL Connection Configurations
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Nikhil10@",
    "database": "phishing_db",
    "port": 3306
}

# Run startup table initialization safely
def init_db():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scan_history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        url VARCHAR(500),
        result VARCHAR(50),
        scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    db.commit()
    cursor.close()
    db.close()

init_db()

# def extract_features(url):
#     parsed = urlparse(url)

#     return [[
#         len(url),                          # URL length
#         url.count('.'),                    # Dot count
#         url.count('-'),                    # Hyphen count
#         int('@' in url),                   # @ symbol
#         int('https' in url),               # HTTPS
#         int('login' in url.lower()),
#         int('verify' in url.lower()),
#         int('secure' in url.lower()),
#         int('update' in url.lower()),
#         len(parsed.netloc),                # Domain length
#         sum(c.isdigit() for c in url),     # Digit count
#         int(re.search(r'\d+\.\d+\.\d+\.\d+', url) is not None) # IP address
#     ]]

def extract_features(url):
    return [[
        len(url),
        url.count('.'),
        int("https" in url),
        int("login" in url.lower())
    ]]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    confidence = 0
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        # prediction = model.predict(features) # Extract the base prediction element
        prediction = model.predict(features)[0]
        confidence = max(model.predict_proba(features)[0]) * 100
        confidence = round(confidence, 2)
        if prediction == 1:
            result = "Phishing Website"
        else:
            result = "Safe Website"

        # Open connection to save log
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        
        sql = "INSERT INTO scan_history (url, result) VALUES (%s, %s)"
        cursor.execute(sql, (url, result))
        db.commit()
        
        cursor.close()
        db.close()

    return render_template("index.html",result=result,confidence=confidence)
    # return render_template("index.html", result=result)

@app.route("/history")
def history():
    # Open connection to fetch history logs
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    
    cursor.execute("SELECT id, url, result, scan_time FROM scan_history ORDER BY scan_time DESC")
    data = cursor.fetchall()
    
    cursor.close()
    db.close()

    return render_template("history.html", records=data)

@app.route("/dashboard")
def dashboard():

    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    cursor.execute("""
    SELECT result, COUNT(*)
    FROM scan_history
    GROUP BY result
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)