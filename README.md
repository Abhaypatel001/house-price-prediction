# 🏠 House Price Prediction using AI/ML

## 🌐 Live Demo

🔗 https://house-price-prediction-wheat.vercel.app

A Machine Learning based House Price Prediction web application built using **Python, Flask, HTML, CSS, JavaScript, and Scikit-learn**. This project predicts the estimated price of a house based on user inputs such as **living area, bedrooms, bathrooms, floors, waterfront, and grade**.

---

## 🚀 Features

- 🏡 Predicts house prices using Machine Learning
- ⚡ Real-time price prediction
- 🎨 Clean and responsive user interface
- 🧠 Trained using Linear Regression
- 🌐 Flask-based backend
- 📊 Accepts multiple house features as input
- 📱 Mobile-friendly design
- 🚀 Ready for deployment on Vercel, Railway, or Render

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 📂 Project Structure

```text
house-price-prediction/
│
├── app.py                  # Flask application
├── train_model.py          # Model training script
├── model.pkl               # Trained ML model
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation
├── .gitignore              # Git ignored files
│
├── templates/
│   └── index.html          # Main HTML page
│
├── static/
│   ├── style.css           # CSS styling
│   └── script.js           # JavaScript
│
├── dataset/
│   └── house_data.csv      # Dataset (optional)
│
└── screenshots/
    ├── home.png
    └── prediction.png
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Abhaypatel001/house-price-prediction.git
```

### 2️⃣ Go to Project Folder

```bash
cd house-price-prediction
```

### 3️⃣ Create Virtual Environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📊 Input Features

| Feature | Description |
|---------|-------------|
| Area | Living area (sqft) |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Floors | Number of floors |
| Waterfront | 0 = No, 1 = Yes |
| Grade | House quality grade |

---

## 🧠 Machine Learning Model

- Algorithm: Linear Regression
- Library: Scikit-learn
- Training Language: Python

---

## 📸 Screenshots

### Home Page

_Add screenshot here_

### Prediction Result

_Add screenshot here_

---

## 📦 requirements.txt

```text
Flask
numpy
pandas
scikit-learn
joblib
gunicorn
```

---

## 🚀 Deployment

This project can be deployed on:

- Vercel
- Railway
- Render

---

## 👨‍💻 Author

**Abhay Patel**

- GitHub: https://github.com/Abhaypatel001
- LinkedIn: Add your LinkedIn profile here

---

## ⭐ Support

If you like this project, don't forget to ⭐ star this repository.
