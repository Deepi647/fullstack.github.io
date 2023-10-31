from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydbs"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Insert data into the MySQL database
    insert_query = "INSERT INTO user_data (name, email) VALUES (%s, %s)"
    cursor.execute(insert_query, (name, email))
    db.commit()

    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
