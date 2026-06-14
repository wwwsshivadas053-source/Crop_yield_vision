# =========================================================
# IMPORTS
# =========================================================

from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import sqlite3
import pickle
import numpy as np
import random
import os
from flask import jsonify
from dotenv import load_dotenv

load_dotenv()



# =========================================================
# FLASK APP
# =========================================================

app = Flask(__name__)
load_dotenv()
# SECRET KEY
app.secret_key = os.environ.get("SECRET_KEY", "yieldvision_secret")

# =========================================================
# DATABASE CONFIGURATION
# =========================================================


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db():

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)

    conn.row_factory = sqlite3.Row

    return conn

# =========================================================
# CREATE DATABASE TABLES
# =========================================================

def init_db():

    conn = get_db()
    cur = conn.cursor()

    # USERS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone_number TEXT,
        password TEXT NOT NULL
    )
    """)

    # FEEDBACK
    cur.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        rating INTEGER,
        message TEXT
    )
    """)

    # PREDICTIONS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        crop INTEGER,
        soil INTEGER,
        temperature REAL,
        rainfall REAL,
        fertilizer INTEGER,
        predicted_yield REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ADMINS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS admins(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

conn = get_db()
cur = conn.cursor()

cur.execute(
    "SELECT * FROM admins WHERE username=?",
    ("admin",)
)

admin = cur.fetchone()

if not admin:

    cur.execute(
        """
        INSERT INTO admins(username,password)
        VALUES(?,?)
        """,
        (
            "admin",
            generate_password_hash("admin123")
        )
    )

    conn.commit()

conn.close()

# =========================================================
# LOAD ML MODEL
# =========================================================

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))

# =========================================================
# EMAIL CONFIGURATION
# =========================================================

app.config['MAIL_SERVER'] = 'smtp.gmail.com'

app.config['MAIL_PORT'] = 587

app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USE_SSL'] = False

# FOR LOCAL TESTING
# CHANGE THESE VALUES

app.config['MAIL_USERNAME'] = 'tsprajwal2@gmail.com'

app.config['MAIL_PASSWORD'] = 'wgja maej oeux xpar'

app.config['MAIL_DEFAULT_SENDER'] = 'tsprajwal2@gmail.com'

mail = Mail(app)

# =========================================================
# LOGIN
# =========================================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        conn = get_db()

        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE email=?", (email,))

        user = cur.fetchone()

        conn.close()

        if user and check_password_hash(user["password"], password):

            session["user"] = user["name"]

            session["email"] = user["email"]

            return redirect(url_for("home"))

        else:

            return "Invalid Email or Password"

    return render_template("login.html")

# =========================================================
# REGISTER
# =========================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get["name"]

        email = request.form.get["email"]

        phone_number = request.form.get["phone_number"]

        password = request.form.get["password"]

        confirm_password = request.form.get["confirm_password"]

        if password != confirm_password:

            return "Passwords do not match!"

        hashed_password = generate_password_hash(password)

        conn = get_db()

        cur = conn.cursor()

        try:

            cur.execute("""
            INSERT INTO users(name, email, phone_number, password)
            VALUES(?,?,?,?)
            """, (name, email, phone_number, hashed_password))

            conn.commit()

        except sqlite3.IntegrityError:

            conn.close()

            return "Email already exists!"

        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.pop("user", None)

    session.pop("email", None)

    return redirect(url_for("login"))

# =========================================================
# HOME PAGE
# =========================================================

@app.route("/home")
def home():

    if "user" not in session:

        return redirect(url_for("login"))

    return render_template("index.html")

# =========================================================
# PREDICTION PAGE
# =========================================================

@app.route("/prediction")
def prediction():

    if "user" not in session:

        return redirect(url_for("login"))

    return render_template("prediction.html")

# =========================================================
# PREDICT CROP YIELD
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        crop = int(request.form["crop"])
        soil = int(request.form["soil"])
        temp = float(request.form["temp"])
        rain = float(request.form["rain"])
        fertilizer = int(request.form["fertilizer"])

        features = np.array([
            [crop, soil, temp, rain, fertilizer]
        ])

        prediction = float(model.predict(features)[0])

        # SAVE TO DATABASE

        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO predictions(
            user_email,
            crop,
            soil,
            temperature,
            rainfall,
            fertilizer,
            predicted_yield
        )
        VALUES(?,?,?,?,?,?,?)
        """, (
            session.get("email"),
            crop,
            soil,
            temp,
            rain,
            fertilizer,
            prediction
        ))

        conn.commit()
        conn.close()

        # FEATURE IMPORTANCE

        importance = model.feature_importances_

        labels = [
            "Crop",
            "Soil",
            "Temperature",
            "Rainfall",
            "Fertilizer"
        ]

        # TEMPERATURE SIMULATION

        temps = list(range(10, 40))

        yields = []

        for t in temps:

            f = np.array([
                [crop, soil, t, rain, fertilizer]
            ])

            y = model.predict(f)[0]

            yields.append(round(float(y), 2))

        return render_template(
            "dashboard.html",
            result=round(prediction, 2),
            labels=labels,
            importance=list(importance),
            temps=temps,
            yields=yields
        )

    except Exception as e:

        return f"Prediction Error: {str(e)}"
# =========================================================
# RECOMMENDATION PAGE
# =========================================================

@app.route("/recommendation")
def recommendation():

    return render_template("recommendation.html")

# =========================================================
# ABOUT PAGE
# =========================================================

@app.route("/about")
def about():

    return render_template("about.html")

# =========================================================
# FEEDBACK PAGE
# =========================================================

@app.route("/feedback")
def feedback():

    conn = get_db()

    cur = conn.cursor()

    cur.execute("SELECT * FROM feedback ORDER BY id DESC")

    reviews = cur.fetchall()

    conn.close()

    return render_template(
        "feedback.html",
        reviews=reviews
    )

# =========================================================
# SUBMIT FEEDBACK
# =========================================================

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():

    try:

        name = request.form["name"]

        email = request.form["email"]

        rating = request.form["rating"]

        message = request.form["message"]

        conn = get_db()

        cur = conn.cursor()

        cur.execute("""
        INSERT INTO feedback(name, email, rating, message)
        VALUES(?,?,?,?)
        """, (name, email, rating, message))

        conn.commit()

        conn.close()

        return redirect(url_for("feedback"))

    except Exception as e:

        return str(e)


# =========================================================
# FORGOT PASSWORD ROUTE
# =========================================================

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]

        # CHECK USER

        conn = get_db()

        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        user = cur.fetchone()

        conn.close()

        if not user:

            return "Email not registered!"

        # GENERATE OTP

        otp = str(random.randint(100000, 999999))

        # STORE OTP IN SESSION

        session["otp"] = otp

        session["reset_email"] = email

        # =========================================================
        # CREATE EMAIL
        # =========================================================

        msg = Message(
            subject="YieldVision Password Reset OTP",
            recipients=[email]
        )

        # TEXT EMAIL

        msg.body = f"""
Hello {user['name']},

We received a request to reset your YieldVision account password.

Your One-Time Password (OTP) is:

{otp}

This OTP is valid for 10 minutes.

If you did not request a password reset, please ignore this email.

Thank you,
YieldVision Support Team
"""

        # HTML EMAIL

        msg.html = f"""
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
</head>

<body style="
    margin:0;
    padding:0;
    background-color:#f4f4f4;
    font-family:Arial, sans-serif;
">

    <table width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <td align="center">

                <table width="600" cellpadding="0" cellspacing="0"
                    style="
                    background:white;
                    margin-top:40px;
                    border-radius:10px;
                    overflow:hidden;
                    box-shadow:0 2px 10px rgba(0,0,0,0.1);
                ">

                    <!-- HEADER -->

                    <tr>
                        <td style="
                            background:#2e7d32;
                            color:white;
                            text-align:center;
                            padding:25px;
                            font-size:28px;
                            font-weight:bold;
                        ">
                            YieldVision
                        </td>
                    </tr>

                    <!-- CONTENT -->

                    <tr>
                        <td style="padding:40px;">

                            <h2 style="
                                color:#333333;
                                margin-top:0;
                            ">
                                Password Reset Request
                            </h2>

                            <p style="
                                font-size:16px;
                                color:#555555;
                                line-height:1.6;
                            ">
                                Hello <b>{user['name']}</b>,
                            </p>

                            <p style="
                                font-size:16px;
                                color:#555555;
                                line-height:1.6;
                            ">
                                We received a request to reset your
                                YieldVision account password.
                            </p>

                            <p style="
                                font-size:16px;
                                color:#555555;
                            ">
                                Use the OTP below to continue:
                            </p>

                            <!-- OTP BOX -->

                            <div style="
                                text-align:center;
                                margin:30px 0;
                            ">

                                <span style="
                                    display:inline-block;
                                    background:#e8f5e9;
                                    color:#2e7d32;
                                    font-size:36px;
                                    letter-spacing:8px;
                                    padding:18px 35px;
                                    border-radius:10px;
                                    font-weight:bold;
                                ">
                                    {otp}
                                </span>

                            </div>

                            <p style="
                                font-size:15px;
                                color:#777777;
                                line-height:1.6;
                            ">
                                This OTP is valid for the next
                                <b>10 minutes</b>.
                            </p>

                            <p style="
                                font-size:15px;
                                color:#777777;
                                line-height:1.6;
                            ">
                                If you did not request this password reset,
                                you can safely ignore this email.
                            </p>

                        </td>
                    </tr>

                    <!-- FOOTER -->

                    <tr>
                        <td style="
                            background:#f1f1f1;
                            text-align:center;
                            padding:20px;
                            font-size:14px;
                            color:#777777;
                        ">

                            © 2026 YieldVision <br>

                            Smart Agriculture Prediction System

                        </td>
                    </tr>

                </table>

            </td>
        </tr>
    </table>

</body>
</html>
"""

        # =========================================================
        # SEND MAIL
        # =========================================================

        try:

            mail.send(msg)

            return redirect(
                url_for("verify_otp")
            )

        except Exception as e:

            return f"Mail Error: {str(e)}"

    return render_template("forgot_password.html")



# =========================================================
# VERIFY OTP
# =========================================================

@app.route("/verify_otp", methods=["GET", "POST"])
def verify_otp():

    if request.method == "POST":

        user_otp = request.form["otp"]

        if user_otp == session.get("otp"):

            return redirect(
                url_for("reset_password")
            )

        else:

            return "Invalid OTP!"

    return render_template("verify_otp.html")

# =========================================================
# RESET PASSWORD
# =========================================================

@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():

    if request.method == "POST":

        password = request.form["password"]

        confirm_password = request.form["confirm_password"]

        if password != confirm_password:

            return "Passwords do not match!"

        hashed_password = generate_password_hash(password)

        conn = get_db()

        cur = conn.cursor()

        cur.execute("""
        UPDATE users
        SET password=?
        WHERE email=?
        """, (
            hashed_password,
            session["reset_email"]
        ))

        conn.commit()

        conn.close()

        # CLEAR SESSION

        session.pop("otp", None)

        session.pop("reset_email", None)

        return redirect(url_for("login"))

    return render_template("reset_password.html")

# =========================================================
# TEST DATABASE
# =========================================================

@app.route("/test_db")
def test_db():

    try:

        conn = get_db()

        cur = conn.cursor()

        cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table';
        """)

        data = cur.fetchall()

        conn.close()

        return str(data)

    except Exception as e:

        return str(e)

# =========================================================
# TEST MAIL
# =========================================================

@app.route("/test_mail")
def test_mail():

    try:

        msg = Message(
            "YieldVision Test Mail",
            recipients=[
                app.config['MAIL_USERNAME']
            ]
        )

        msg.body = """
Mail is working successfully.
"""

        mail.send(msg)

        return "Mail Sent Successfully"

    except Exception as e:

        return f"Mail Error: {str(e)}"

@app.route("/admin", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM admins WHERE username=?",
            (username,)
        )

        admin = cur.fetchone()

        conn.close()

        if admin and check_password_hash(
            admin["password"],
            password
        ):
            session["admin"] = admin["username"]
            return redirect(url_for("admin_dashboard"))

        return "Invalid Admin Credentials"

    return render_template("admin_login.html")

@app.route("/admin/dashboard")
def admin_dashboard():

    if "admin" not in session:
        return redirect(url_for("admin_login"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    total_users = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM predictions")
    total_predictions = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM feedback")
    total_feedback = cur.fetchone()[0]

    cur.execute(
        "SELECT AVG(predicted_yield) FROM predictions"
    )

    avg_yield = cur.fetchone()[0] or 0

    cur.execute("""
                SELECT *
                FROM predictions
                ORDER BY id DESC LIMIT 10
                """)

    recent_predictions = cur.fetchall()

    conn.close()

    return render_template(
        "admin_dashboard.html",
        total_users=total_users,
        total_predictions=total_predictions,
        total_feedback=total_feedback,
        avg_yield=round(avg_yield, 2),
        recent_predictions=recent_predictions
    )


@app.route("/admin/logout")
def admin_logout():

    session.pop("admin", None)

    return redirect(url_for("admin_login"))

@app.route("/admin/users")
def admin_users():

    if "admin" not in session:
        return redirect(url_for("admin_login"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    users = cur.fetchall()

    conn.close()

    return render_template(
        "admin_users.html",
        users=users
    )


@app.route("/admin/predictions")
def admin_predictions():

    if "admin" not in session:
        return redirect(url_for("admin_login"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM predictions
    ORDER BY id DESC
    """)

    predictions = cur.fetchall()

    conn.close()

    return render_template(
        "admin_predictions.html",
        predictions=predictions
    )


@app.route("/admin/feedback")
def admin_feedback():

    if "admin" not in session:
        return redirect(url_for("admin_login"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM feedback
    ORDER BY id DESC
    """)

    reviews = cur.fetchall()

    conn.close()

    return render_template(
        "admin_feedback.html",
        reviews=reviews
    )


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)
