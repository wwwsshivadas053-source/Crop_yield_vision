🌾 Smart Crop Recommendation & Agricultural Assistant

A Flask-based web application that helps farmers and agriculture enthusiasts make informed decisions by providing crop recommendations, fertilizer suggestions, crop yield predictions, and AI-powered agricultural assistance.

🚀 Features
🌱 Crop Recommendation
Recommends the most suitable crop based on:
Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
pH Value
Rainfall

🧪 Fertilizer Recommendation
Suggests appropriate fertilizers based on:
Soil Type
Crop Type
Nutrient Levels

📈 Crop Yield Prediction
Predicts expected crop yield using Machine Learning models.
Helps farmers estimate production before cultivation.

🤖 AI Agricultural Assistant
Integrated with Google Gemini AI.
Answers agriculture-related questions.
Provides farming guidance and best practices.

📧 Contact & Feedback System
Users can send queries through the contact form.
Email notifications using Flask-Mail.

🔒 Secure Authentication
User Registration
Login System
Session Management

🛠️ Technologies Used
Frontend
HTML5
CSS3
Bootstrap 5
JavaScript
Backend
Python
Flask
Machine Learning
Scikit-Learn
NumPy
AI Integration
Google Gemini API
Database
SQLite
Deployment
Render
Gunicorn

📂 Project Structure
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── database.db
├── model.pkl
├── crop_encoder.pkl
├── soil_encoder.pkl
├── fertilizer_encoder.pkl
├── templates/
├── static/
└── README.md

⚙️ Installation
Clone Repository
git clone https://github.com/yourusername/smart-crop-recommendation.git
cd smart-crop-recommendation
Create Virtual Environment
python -m venv venv
Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Configure Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

Run Application
python app.py

Open:

http://127.0.0.1:5000
🚀 Deployment on Render
Build Command
pip install -r requirements.txt
Start Command
gunicorn app:app
Environment Variables
SECRET_KEY=your_secret_key
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password


👨‍💻 Author

Prajwal T.S.

BCA Graduate
Machine Learning & Generative AI Enthusiast
Passionate about AI-powered Agriculture Solutions
📜 License

This project is developed for educational and research purposes. Feel free to use and modify it for learning and non-commercial applications.
