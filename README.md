# 🌾 Crop Yield Prediction & Recommendation System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

> An intelligent **Crop Yield Prediction & Recommendation System** powered by **Machine Learning**, **Flask**, and **Google Gemini AI**. The application predicts crop yield using agricultural parameters and provides AI-generated farming recommendations to help farmers and researchers make data-driven decisions.

---

# 📌 Table of Contents

- Overview
- Features
- Tech Stack
- Project Structure
- Machine Learning Model
- Installation
- Environment Variables
- Running the Application
- Application Workflow
- Screenshots
- Future Enhancements
- Deployment
- Contributing
- License

---

# 🌱 Overview

Agriculture plays a significant role in the global economy. Predicting crop yield accurately enables farmers to optimize cultivation strategies, improve productivity, and efficiently manage available resources.

This project combines **Machine Learning**, **Flask**, **SQLite**, and **Google Gemini AI** to deliver a complete smart agriculture solution with:

- Crop Yield Prediction
- AI Crop Recommendation
- Secure User Authentication
- Admin Dashboard
- Prediction History
- Feedback Management

---

# ✨ Features

## 👨‍🌾 User Features

- User Registration
- Secure Login
- Forgot Password (OTP Verification)
- Password Reset
- User Dashboard
- Crop Yield Prediction
- AI Crop Recommendation
- Prediction History
- Feedback Submission
- Responsive Interface

---

## 🤖 AI Features

- Google Gemini AI Integration
- Smart Crop Recommendation
- Farming Guidance
- Agricultural Best Practices
- Irrigation Suggestions
- Fertilizer Recommendations
- Soil Improvement Advice

---

## 📈 Machine Learning

- Crop Yield Prediction
- Trained Regression Model
- Label Encoding
- Data Preprocessing
- Fast Predictions
- Scikit-Learn Model Serialization

---

## 🔐 Authentication

- Password Hashing
- Secure Sessions
- OTP Password Recovery
- Protected User Routes
- Admin Authentication

---

## 👨‍💼 Admin Panel

Administrator can:

- View Registered Users
- Monitor Crop Predictions
- View User Feedback
- Dashboard Analytics
- Manage Application Data

---

# 🛠 Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript

---

## Backend

- Python
- Flask
- SQLite
- Flask-Mail
- Werkzeug

---

## Machine Learning

- Scikit-Learn
- NumPy
- Pickle

---

## AI

- Google Gemini API

---

# 📂 Project Structure

```
crop/
│
├── app.py
├── database.db
├── model.pkl
├── crop_encoder.pkl
├── soil_encoder.pkl
├── fertilizer_encoder.pkl
├── crop_yield.csv
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── static/
│   ├── style.css
│   ├── dashboard.js
│   └── growth.png
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── prediction.html
│   ├── recommendation.html
│   ├── feedback.html
│   ├── forgot_password.html
│   ├── verify_otp.html
│   ├── reset_password.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   ├── admin_users.html
│   ├── admin_predictions.html
│   ├── admin_feedback.html
│   └── about.html
│
└── README.md
```

---

# ⚙️ Machine Learning Workflow

```
User Input
      │
      ▼
Data Validation
      │
      ▼
Feature Encoding
      │
      ▼
Machine Learning Model
      │
      ▼
Yield Prediction
      │
      ▼
Gemini AI Recommendation
      │
      ▼
Display Results
```

---

# 📊 Prediction Parameters

The prediction model uses agricultural inputs such as:

- Crop Type
- Soil Type
- Fertilizer Type
- Temperature
- Rainfall

The trained Machine Learning model estimates the expected crop yield based on these parameters.

---

# 🤖 AI Crop Recommendation

After prediction, Google Gemini AI provides intelligent recommendations including:

- Suitable Crops
- Fertilizer Advice
- Soil Health Tips
- Irrigation Suggestions
- Pest Prevention Tips
- Farming Best Practices

---

# 🔐 Security Features

- Password Hashing
- OTP Verification
- Session Management
- Protected Routes
- Input Validation
- SQL Injection Prevention

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/crop-yield-prediction.git

cd crop-yield-prediction
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key

MAIL_USERNAME=your_email@gmail.com

MAIL_PASSWORD=your_gmail_app_password
```

> Never expose API keys or email passwords in your source code.

---

# ▶️ Running the Project

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 👨‍💻 Admin Login

Default Administrator Credentials

```
Username : admin

Password : admin123
```

**Change the default credentials before deploying the application to production.**

---

# 📷 Screenshots

Create a folder:

```
screenshots/
```

Example:

```
screenshots/

login.png

register.png

dashboard.png

prediction.png

recommendation.png

feedback.png

admin_login.png

admin_dashboard.png
```

Use them inside README.

```markdown
## Login

![Login](screenshots/login.png)

## Dashboard

![Dashboard](screenshots/dashboard.png)

## Prediction

![Prediction](screenshots/prediction.png)

## Recommendation

![Recommendation](screenshots/recommendation.png)

## Admin Dashboard

![Admin](screenshots/admin_dashboard.png)
```

---

# 📦 Requirements

Main libraries:

```
Flask

Flask-Mail

Werkzeug

NumPy

Scikit-Learn

python-dotenv

google-generativeai
```

Install:

```bash
pip install -r requirements.txt
```

---

# 🌍 Deployment

This project can be deployed on:

- Render
- Railway
- PythonAnywhere
- Azure App Service
- Heroku
- AWS Elastic Beanstalk
- DigitalOcean

---

# 🚀 Future Enhancements

- Weather API Integration
- Fertilizer Prediction Model
- Crop Disease Detection
- Satellite Image Analysis
- Interactive Analytics Dashboard
- PDF Report Generation
- Mobile Application
- SMS Notifications
- Voice Assistant
- Multi-language Support
- Cloud Database Integration

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.

2. Create your feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Prajwal T. S.**

AI • Machine Learning • Python • Flask • Data Science

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ Show Your Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

💡 Share it with others

🤝 Contribute to the project

---

# 🌾 Empowering Smart Agriculture with Artificial Intelligence.
