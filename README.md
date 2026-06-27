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


<img width="1364" height="637" alt="re" src="https://github.com/user-attachments/assets/fb192239-501d-4603-83ba-7500c4524d7f" />
<img width="1366" height="637" alt="log" src="https://github.com/user-attachments/assets/013342ab-c8b6-4eb1-a741-8b5e2131956f" />
<img width="1354" height="635" alt="hom" src="https://github.com/user-attachments/assets/4f85c515-d527-4947-b300-e8edbfc8b751" />
<img width="1349" height="635" alt="abou" src="https://github.com/user-attachments/assets/7cc1e6a2-030c-48f4-9a92-8b942db72046" />
<img width="1351" height="640" alt="Screenshot 2026-06-26 190135" src="https://github.com/user-attachments/assets/19601f16-dccc-4003-b53b-697385b1a6f9" />
<img width="1349" height="640" alt="das" src="https://github.com/user-attachments/assets/5f5449f9-dedd-46fa-a6c4-fbd9af8da443" />
<img width="1349" height="637" alt="recom" src="https://github.com/user-attachments/assets/947b789c-b2bb-4e85-a5f5-19179e513db3" />
<img width="1347" height="641" alt="f1" src="https://github.com/user-attachments/assets/db2786a0-bcfc-44d0-9380-9a5cd9d84bee" />
<img width="1348" height="621" alt="f2" src="https://github.com/user-attachments/assets/a6523b68-ce3f-4ac1-8771-2afd7e7ad624" />
<img width="1366" height="634" alt="ad log" src="https://github.com/user-attachments/assets/1aa8ac03-03f4-4810-bf60-5a1e42ea4510" />
<img width="1348" height="637" alt="ad dash" src="https://github.com/user-attachments/assets/40cc0546-538b-4b4a-a688-42d72f4d2861" />
<img width="1350" height="636" alt="ad dash2" src="https://github.com/user-attachments/assets/6a4949f9-1f88-4c30-ac76-f889f858ac14" />
<img width="1366" height="634" alt="predi" src="https://github.com/user-attachments/assets/4775f7d9-9c7b-4b23-8f82-c484583022e7" />
<img width="1347" height="636" alt="ad feed" src="https://github.com/user-attachments/assets/a2afee9c-eb2e-44d9-8971-382f7c0cf6a6" />


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

GitHub: https://github.com/wwwsshivadas053-source

LinkedIn: https://www.linkedin.com/in/prajwal-t-s-354a57359

---

# ⭐ Show Your Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

💡 Share it with others

🤝 Contribute to the project

---

# 🌾 Empowering Smart Agriculture with Artificial Intelligence.
