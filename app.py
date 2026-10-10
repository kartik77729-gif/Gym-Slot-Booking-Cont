from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_user_data():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM Users"))
        result_all = result.mappings().all()
        print(result_all)

        if result_all:
            first_result_dict = dict(result_all[0])
            print('type of', type(first_result_dict), 'is', first_result_dict)
            return 
        else:
            print("The Users table is empty.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bookings')
def bookings():
    return render_template('booking.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dbtest')
def dbtest():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return f"DB connected: {result.scalar()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)