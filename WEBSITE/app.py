from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'churchrms_db'

mysql = MySQL(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        mysql.connection.commit()
        cur.close()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/')
def Index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customers")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', customers = data)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[2], password):
            session['logged_in'] = True
            session['username'] = username
            flash("Login Successful!", "success")
            return redirect(url_for('dashboard'))
        else:
               flash("Invalid Username or Password", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash("You have been logged out", "info")
    return redirect(url_for('login'))

@app.route('/insert', methods=['POST'])
def insert():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        flash("Data Inserted Succesfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)", (name,email,phone))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['POST', 'GET'])
def delete(id_data):
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    flash("Data Deleted Succesfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customers WHERE id = %s", (id_data,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('Index'))

@app.route('/update', methods=['POST', 'GET'])
def update():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
                    UPDATE customers
                    SET name = %s, email = %s, phone = %s
                    WHERE id = %s
                    """, (name, email, phone, id_data))
        
        flash("Data Updated Sucessfully")
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('Index'))

@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        flash("You must be logged in to access the dashboard.", "warning")
        return redirect(url_for('login'))

    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)