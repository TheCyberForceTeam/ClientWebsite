import sqlite3
from datetime import datetime
import os
from flask import Flask, request, redirect, render_template, session, url_for
from flask_mail import Mail, Message
import time
import csv
import matplotlib.pyplot as plt
import io


secret_key = os.urandom(24).hex()
print(secret_key)

app = Flask(__name__,static_folder='static', template_folder='/users/nathanbrown-bennett/Programming/Web Server/ClientWebsite/')
app.secret_key = secret_key
current_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#Emailus setup
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'thecyberforceteam@gmail.com'
app.config['MAIL_PASSWORD'] = 'pyumtfhyertwwniw'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#Log.py initialisation so that each time a user logs in, it is recorded in the log file with their username, time of login and IP address
def log(username, ip): 
    with open('log.txt', 'a') as file:
        file.write(f"{username} logged in at {current_time} from IP address {ip}\n")

# database initialization
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = [row[0] for row in c.fetchall()]
for table_name in table_names:
    c.execute(f"SELECT * FROM {table_name}")
    table_data = c.fetchall()
    print(f"{table_name} data: {table_data}")
conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        if session['is_staff']:
            return redirect(url_for('staff'))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['Email']
    password = request.form['Password']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Check if the user exists in the staff table
    user = c.execute("SELECT * FROM Staff WHERE email = ? AND password = ?", (email, password)).fetchone()
    if user:
        session['email'] = user[1]
        session['is_staff'] = True
    
        ip = request.remote_addr
        c.execute("UPDATE Staff SET last_login_date = ?, last_login_ip_address = ?, successful_logins = successful_logins + 1, \
                   total_login_attempts = 0 WHERE email = ?", (current_time, ip, email))
        log(email, ip)
        conn.commit()
        conn.close()
    
        return redirect(url_for('staff'))
    else:
        # Check if the user exists in the Users table
        user = c.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (email, password)).fetchone()
    
        if user:
            session['email'] = user[1]
            session['is_staff'] = False # Set to False for users
    
            ip = request.remote_addr
            c.execute("UPDATE Users SET last_login_date = ?, last_login_ip_address = ?, successful_logins = successful_logins + 1, \
                       total_login_attempts = 0 WHERE username = ?", (current_time, ip, email))
            log(email, ip)
            conn.commit()
            conn.close()
    
            if user[7]:
                return redirect(url_for('staff'))
            else:
                return redirect(url_for('home'))
        else:
            session.pop('email', None)
            session.pop('is_staff', None)
            ip = request.remote_addr
    
            # Check if the user exists in the staff table
            user = c.execute("SELECT * FROM Staff WHERE email = ?", (email,)).fetchone()
            if user:
                c.execute("UPDATE Staff SET total_login_attempts = total_login_attempts + 1, unsuccessful_logins = unsuccessful_logins + 1 \
                           WHERE email = ? + WHERE last_login_ip_address = ?", (email,ip))
                log(email, ip)
                if user[5] + 1 >= 5:
                    return redirect(url_for('reset_password', email=email))
            else:
                c.execute("INSERT INTO Users (username, password, total_login_attempts, unsuccessful_logins, last_login_ip_address) \
                           VALUES (?, ?, 1, 1)", (email, password, ip))
                log(email, ip)
            conn.commit()
            conn.close()
    
            return redirect(url_for('failed_login.html'))
        
@app.route('/failed_login.html')
def failed_login():
    time.sleep(5)
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['Email']
    password = request.form['Password']
    username = session["username"]
    
    ip = request.remote_addr

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Check if the user already exists in the database
    user = c.execute("SELECT * FROM Users WHERE email = ?", (email,)).fetchone()

    if user:
        # If the user already exists, reset their password and send them an email with their new password
        new_password = 'SuperSecretPassword3'  # Replace with a randomly generated password
        log(email, ip)
        c.execute("UPDATE Users SET password = ?, total_login_attempts = 0, last_login_ip_address = ?, last_login_date = ? WHERE email = ?, WHERE username = ?", (new_password, request.remote_addr, current_time, email, username))
        conn.commit()
        conn.close()

        msg = Message('Password Reset', sender='thecyberforceteam@gmail.com', recipients=[email])
        msg.body = f'Your password has been reset to {new_password}. Please use this new password to log in.'
        mail.send(msg)

        return redirect(url_for('index'))
    else:
        # If the user doesn't exist, create a new user in the database
        username = session["username"]
        successful_logins = 0
        unsuccessful_logins = 0
        total_login_attempts = 0
        last_login_ip_address = request.remote_addr
        last_login_date = current_time
        address = ''
        phone = ''
        is_staff = 0
        user_data = (email, username, password, successful_logins, unsuccessful_logins, total_login_attempts,
                     last_login_ip_address, last_login_date, address, phone, is_staff)
        log(username, ip)

        c.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", user_data)
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

@app.route('/emailus', methods=['POST'])
def email():
    sender_name = request.form['Name']
    sender_email = request.form['Email']
    subject = request.form.get('Subject', '')
    message = request.form['Message']
    print(f"Sender Name: {sender_name}, Sender Email: {sender_email}, Subject: {subject}, Message: {message}")
    msg = Message(subject=subject, sender=(sender_name, sender_email), recipients=["thecyberforceteam@gmail.com"])
    msg.body = message
    mail.send(msg)
    return app.send_static_file('emailsent.html')

@app.route('/emailsent.html')
def emailsent():
    return redirect(url_for('index'))
    

@app.route('/home')
def home():
    ip = request.remote_addr
    if 'username' in session and not session['is_staff']:
        username = session['username']
        c.execute("UPDATE Users SET last_login_ip_address = ?, last_login_date = ? WHERE email = ?, WHERE username = ?", (request.remote_addr, current_time, email, username))
        log(username, ip)
        conn.commit()
        return render_template('index.html', username=username)
    else:
        return render_template('index.html', username='Guest')

@app.route('/createbarchart', methods=['POST'])
def create_bar_chart():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT Name, Age FROM table')
    data = c.fetchall()
    c.close()
    conn.close()
    names = [x[0] for x in data]
    ages = [x[1] for x in data]
    plt.bar(names, ages)
    plt.savefig('static/bar_chart.png')
    plt.close()
    return redirect(url_for('staff'))

@app.route('/staff',methods=['GET', 'POST'])
def staff():
    username = session['username']
    if 'username' in session and session['is_staff']:
        username = session['username']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        ip = request.remote_addr
        c.execute("UPDATE Users SET successful_logins = successful_logins + 1 WHERE username = ?", (username,))
        log(username, ip)
        conn.commit()
        c.execute('SELECT * FROM table')
        data = c.fetchall()
        c.close()
        conn.close()
        return render_template('Staff.html', username=username, data=data)
    else:
        return render_template('index.html', username=username)


@app.route('/download')
def download():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM table')
    data = c.fetchall()
    c.close()
    conn.close()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Name', 'Age'])
    writer.writerows(data)
    output.seek(0)
    return output.getvalue()

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO table (Name, Age) VALUES (?, ?)', (name, age))
    conn.commit()
    c.close()
    conn.close()
    return redirect(url_for('staff'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM table WHERE ID = ?', (id,))
    conn.commit()
    c.close()
    conn.close()
    return redirect(url_for('staff'))

    
@app.route('/News.html', methods=['GET', 'POST'])
def news():
    return app.send_static_file('News.html')

@app.route('/Book.html',methods=['GET', 'POST'])
def book():
    return app.send_static_file('Book.html')

@app.route('/Legal.html',methods=['GET', 'POST'])
def legal():
    return app.send_static_file('Legal.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)