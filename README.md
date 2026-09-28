# 🛡️ ML-Based Phishing Detection System

An **ML-based web application for detecting phishing websites from URLs** using a Random Forest classification model. The system extracts URL-based features, predicts whether a website is **Phishing** or **Safe**, displays prediction confidence, and stores scan results in a MySQL database for historical analysis.

## 🚀 Features

* 🔍 URL-based phishing website detection
* 🤖 Random Forest machine learning classifier
* 📊 Prediction confidence score
* 🗄️ MySQL database integration
* 📜 Scan history tracking
* 📈 Dashboard for analyzing scan results
* 🌐 Flask-based web interface
* 🔄 ARFF-to-CSV dataset conversion support
* 💾 Trained model saved using Joblib

## 🏗️ System Architecture

```text
                ┌─────────────────────┐
                │      User enters    │
                │         URL         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Feature Extraction│
                ├─────────────────────┤
                │ • URL Length        │
                │ • Dot Count         │
                │ • HTTPS Indicator   │
                │ • Login Keyword     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  Random Forest ML   │
                │      Classifier     │
                └──────────┬──────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
        ┌────────────────┐   ┌────────────────┐
        │ Safe Website   │   │Phishing Website│
        └────────────────┘   └────────────────┘
                 │                   │
                 └─────────┬─────────┘
                           ▼
                ┌─────────────────────┐
                │   MySQL Database    │
                │    Scan History     │
                └──────────┬──────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
        ┌────────────────┐   ┌────────────────┐
        │ History Page   │   │   Dashboard    │
        └────────────────┘   └────────────────┘
```

## 🧠 Machine Learning Model

The project uses a **Random Forest Classifier** with 100 decision trees. The dataset is divided into training and testing sets using an 80:20 split.

### Features Used

The current application extracts four features from each URL:

| Feature        | Description                         |
| -------------- | ----------------------------------- |
| `length`       | Total length of the URL             |
| `dots`         | Number of `.` characters            |
| `http_clause`  | Whether `"https"` occurs in the URL |
| `login_clause` | Whether `"login"` occurs in the URL |

These same features are generated during model training and during Flask prediction, keeping the model input consistent.

### Model Training

The training script:

1. Loads `phishing.csv`
2. Extracts URL features
3. Separates features and labels
4. Splits the dataset into training and testing sets
5. Trains a Random Forest classifier
6. Calculates model accuracy
7. Generates a classification report
8. Saves the trained model as `phishing_model.pkl`

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **MySQL**
* **Joblib**
* **SciPy**
* **HTML/CSS**
* **Machine Learning**

## 📂 Project Structure

```text
ML-Based-Phishing-Detection/
│
├── app.py
├── train_model.py
├── convertor.py
├── phishing.csv
├── phishing_model.pkl
│
├── templates/
│   ├── index.html
│   ├── history.html
│   └── dashboard.html
│
├── static/
│   └── ...
│
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ML-Based-Phishing-Detection.git
cd ML-Based-Phishing-Detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask pandas scikit-learn joblib mysql-connector-python scipy
```

## 🗄️ MySQL Configuration

Create a MySQL database:

```sql
CREATE DATABASE phishing_db;
```

The application creates the `scan_history` table automatically when it starts. The table stores:

* Scan ID
* URL
* Prediction result
* Scan timestamp

The Flask application connects to MySQL and records every scanned URL.

> **Security Note:** Never upload real database passwords, API keys, or other credentials to GitHub. Use environment variables or a `.env` file and add `.env` to `.gitignore`.

## 🧪 Train the Model

Make sure `phishing.csv` contains the required URL and result/target columns.

Run:

```bash
python train_model.py
```

The script generates:

```text
phishing_model.pkl
```

This model is then loaded by the Flask application.

## 🔄 Dataset Conversion

If your dataset is provided as an ARFF file, `convertor.py` can convert it into CSV format.

Place:

```text
dataset.arff
```

in the project directory and run:

```bash
python convertor.py
```

The script loads the ARFF dataset using SciPy, converts it into a Pandas DataFrame, and saves it as `dataset.csv`.

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

The application provides:

### 🏠 Home

Enter a URL to receive a prediction.

The application returns:

* **Phishing Website**
* **Safe Website**
* Prediction confidence percentage

The prediction and confidence are generated using the trained model.

### 📜 Scan History

```text
/history
```

Displays previously scanned URLs along with their prediction results and timestamps.

### 📊 Dashboard

```text
/dashboard
```

Provides an aggregated count of safe and phishing scan results.

## 📊 Model Evaluation

The training program calculates:

* Accuracy
* Precision
* Recall
* F1-score
* Classification report

The exact performance depends on the dataset used for training. The project prints the measured accuracy and detailed classification report after training.

## 🔐 Security Considerations

This project is intended as an educational cybersecurity and machine-learning project.

The current model uses only four URL-level features, so it should **not be considered a complete real-world phishing detection solution**.

For a production-grade system, additional features could include:

* Domain age
* WHOIS information
* DNS information
* SSL certificate information
* IP-address detection
* URL redirection analysis
* Suspicious symbols and characters
* Subdomain analysis
* HTML and JavaScript analysis
* Website reputation
* External threat-intelligence feeds

## 🔮 Future Enhancements

* [ ] Add more URL-based features
* [ ] Compare Random Forest with other ML algorithms
* [ ] Add feature importance visualization
* [ ] Improve phishing detection accuracy
* [ ] Add real-time URL reputation checking
* [ ] Add WHOIS and DNS analysis
* [ ] Add SSL certificate analysis
* [ ] Add user authentication
* [ ] Improve dashboard visualizations
* [ ] Deploy the application using a production WSGI server
* [ ] Add REST API support
* [ ] Add automated model retraining

## 🎯 Project Objective

The main objective of this project is to demonstrate how **machine learning can be integrated with a web-based cybersecurity application to identify potentially malicious phishing URLs**.

It combines:

```text
Cybersecurity
      +
Machine Learning
      +
Python
      +
Flask
      +
MySQL
```

## 👨‍💻 Author

**Nikhil Kumar**

B.Tech Computer Science & Engineering Student
Interested in **Cybersecurity, Network Security, Machine Learning, and Research**.

## ⭐ Acknowledgement

This project was developed as an academic and cybersecurity learning project to explore the practical application of machine learning for phishing website detection.

---

### ⚠️ Disclaimer

This project is intended for **educational and research purposes**. Predictions generated by the system should not be treated as a definitive security verdict. Always verify suspicious URLs using multiple trusted security resources.

