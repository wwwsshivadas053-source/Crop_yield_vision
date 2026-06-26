# 🌾 YieldVision AI – Smart Crop Yield Prediction System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-green.svg">
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg">
  <img src="https://img.shields.io/badge/SQLite-Database-blue.svg">
  <img src="https://img.shields.io/badge/License-MIT-success.svg">
</p>

> **YieldVision AI** is a Machine Learning-powered Crop Yield Prediction System that helps farmers, researchers, and agricultural professionals estimate crop yield based on environmental and agricultural factors. The application combines predictive analytics, secure authentication, AI-powered agricultural assistance, and an interactive dashboard into a modern web platform.

---

# 📖 Overview

Agricultural productivity depends on numerous environmental and farming parameters. Predicting crop yield accurately enables farmers to make informed decisions regarding crop selection, fertilizer usage, irrigation planning, and resource management.

YieldVision AI utilizes a trained Machine Learning model to predict expected crop yield using user-provided agricultural data. The system also integrates AI-powered crop recommendations, user management, feedback collection, and an administrator dashboard.

---

# ✨ Features

## 👤 User Features

- User Registration
- Secure Login System
- Password Hashing
- Forgot Password with OTP Verification
- Password Reset
- User Dashboard
- Crop Yield Prediction
- Crop Recommendation
- AI Agricultural Assistant
- Prediction History
- Feedback Submission
- Responsive UI

---

## 🤖 Machine Learning Features

- Crop Yield Prediction
- Trained ML Model
- Label Encoding
- Real-time Prediction
- High-Speed Inference
- Data Preprocessing
- Numerical Feature Processing
- Encoded Categorical Variables

---

## 🧠 AI Features

- AI-powered Crop Recommendation
- Agricultural Guidance
- Farming Tips
- Smart Suggestions
- Gemini AI Integration
- Interactive Chat Responses

---

## 🔐 Authentication

- Secure Password Storage
- Password Hashing
- OTP Verification
- Email-Based Password Recovery
- Session Management
- Protected Routes

---

## 📊 Admin Panel

Administrator can manage:

- Registered Users
- Prediction Records
- User Feedback
- Admin Authentication
- Dashboard Statistics

---

# 🖥️ Screens

- Login
- Registration
- Dashboard
- Crop Prediction
- Crop Recommendation
- Forgot Password
- OTP Verification
- Password Reset
- Feedback
- Admin Login
- Admin Dashboard
- Users Management
- Prediction Management
- Feedback Management

---

# 🛠️ Technology Stack

## Backend

- Python
- Flask
- SQLite
- Flask-Mail
- Google Gemini API
- Pickle

## Frontend

- HTML5
- CSS3
- JavaScript

## Machine Learning

- Scikit-Learn
- NumPy
- Pickle Serialization

## Database

- SQLite

---

# 📂 Project Structure

```
YieldVisionAI/
│
├── app.py
├── model.pkl
├── crop_encoder.pkl
├── fertilizer_encoder.pkl
├── soil_encoder.pkl
├── crop_yield.csv
├── database.db
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── prediction.html
│   ├── recommendation.html
│   ├── feedback.html
│   ├── admin_dashboard.html
│   ├── admin_users.html
│   ├── admin_predictions.html
│   ├── admin_feedback.html
│   └── ...
│
├── static/
│   ├── style.css
│   ├── dashboard.js
│   └── growth.png
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/YieldVisionAI.git

cd YieldVisionAI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

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

Create a `.env` file inside the project directory.

```env
SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key

MAIL_USERNAME=your_email@gmail.com

MAIL_PASSWORD=your_app_password
```

> **Important:** Never hardcode API keys, email passwords, or secret keys into your source code. Store them securely using environment variables.

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📈 Crop Yield Prediction Workflow

```
User Login
      │
      ▼
Dashboard
      │
      ▼
Enter Crop Details
      │
      ▼
Preprocessing
      │
      ▼
Machine Learning Model
      │
      ▼
Yield Prediction
      │
      ▼
Recommendation & Result
```

---

# 🧮 Prediction Parameters

The model predicts crop yield using inputs such as:

- Crop Type
- Soil Type
- Temperature
- Rainfall
- Fertilizer Type

The trained model processes these inputs to estimate the expected crop yield.

---

# 🤖 AI Crop Recommendation

The integrated Gemini AI assists users by providing:

- Suitable crops
- Farming advice
- Agricultural best practices
- Soil recommendations
- Irrigation guidance
- Fertilizer suggestions
- Crop management tips

---

# 🔒 Security Features

- Password Hashing
- Secure Authentication
- Session Protection
- OTP Password Recovery
- Input Validation
- SQL Injection Protection
- Protected Admin Routes

---

# 📊 Admin Dashboard

Administrators can:

- Monitor registered users
- View crop prediction history
- Review user feedback
- Access dashboard analytics
- Manage application records

---

# 📸 Screenshots

Add screenshots inside a folder named:

```
screenshots/
```

Example:

```
screenshots/
├── login.png
├── dashboard.png
├── prediction.png
├── recommendation.png
├── admin_dashboard.png
```

Then include them:

```markdown
## Login

![Login](screenshots/login.png)

## Dashboard

![Dashboard](screenshots/dashboard.png)

## Prediction

![Prediction](screenshots/prediction.png)

## Recommendation

![Recommendation](screenshots/recommendation.png)
```

---

# 🚀 Future Improvements

- Weather API Integration
- Satellite Data Analysis
- Disease Detection
- Fertilizer Recommendation Model
- Soil Nutrient Analysis
- Yield Forecast Charts
- Multi-language Support
- PDF Report Generation
- Cloud Database Integration
- Mobile Application
- SMS Notifications
- Farmer Community Portal

---

# 📦 Dependencies

Major libraries include:

```
Flask

NumPy

Scikit-Learn

Flask-Mail

python-dotenv

google-genai

Werkzeug
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🌍 Deployment

The project can be deployed on:

- Render
- Railway
- PythonAnywhere
- Azure App Service
- AWS Elastic Beanstalk
- Heroku
- DigitalOcean

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📝 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Prajwal T. S.**

AI & Machine Learning Enthusiast

Python | Flask | Machine Learning | Data Science | Full Stack Development

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork it
- 🛠️ Contribute to improve it
- 📢 Share it with others

---

## 🌾 "Empowering Agriculture Through Artificial Intelligence."
