import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import engine
from sqlalchemy import text

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        with engine.connect() as conn:
            user = conn.execute(
                text("SELECT username, password FROM Users WHERE username = :u"),
                {"u": username},
            ).mappings().first()

        if user and user['password'] == password:
            session['username'] = user['username']
            return redirect(url_for('dashboard'))

        error = "Invalid username or password"

    return render_template('index.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/bookings')
def bookings():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('booking.html')