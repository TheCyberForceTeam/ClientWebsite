import sqlite3
from datetime import datetime
import os
from flask import Flask, request, redirect, render_template, session, url_for

secret_key = os.urandom(24).hex()
print(secret_key)

app = Flask(__name__, template_folder='/Users/nathanbrown-bennett/Programming/Web Server/ClientWebsite')
app.secret_key = secret_key

# database initialization
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("SELECT * FROM Staff")
staff_data = c.fetchall()
print(staff_data)
c.execute("SELECT * FROM Admin")
Admin_data = c.fetchall()
print(Admin_data)
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = [row[0] for row in c.fetchall()]
for table_name in table_names:
    c.execute(f"SELECT * FROM {table_name}")
    table_data = c.fetchall()
    print(f"{table_name} data: {table_data}")

c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, last_login TEXT, last_login_ip TEXT, \
           login_attempts INTEGER DEFAULT 0, successful_logins INTEGER DEFAULT 0, failed_logins INTEGER DEFAULT 0, \
           is_staff INTEGER DEFAULT 0, is_admin INTEGER DEFAULT 0)')

# create an admin user if it doesn't exist
admin_user = c.execute("SELECT * FROM users WHERE username = 'admin'").fetchone()
if not admin_user:
    c.execute("INSERT INTO users (username, password, is_admin) VALUES ('admin', 'password', 1)")

# create a staff user if it doesn't exist
staff_user = c.execute("SELECT * FROM users WHERE username = 'staff'").fetchone()
if not staff_user:
    c.execute("INSERT INTO users (username, password, is_staff) VALUES ('staff', 'password', 1)")

conn.commit()

@app.route('/')
def index():
    if 'username' in session:
        if session['is_staff']:
            return redirect(url_for('staff'))
        else:
            return redirect(url_for('home'))
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Check if the user exists in the staff table
    user = c.execute("SELECT * FROM Staff WHERE email = ? AND password = ?", (email, password)).fetchone()

    if user:
        session['email'] = user[2]
        session['is_staff'] = True

        now = datetime.now()
        ip = request.remote_addr
        c.execute("UPDATE users SET last_login = ?, last_login_ip = ?, successful_logins = successful_logins + 1, \
                   login_attempts = 0 WHERE email = ?", (now.strftime("%Y-%m-%d %H:%M:%S"), ip, email))
        conn.commit()
        conn.close()

        return redirect(url_for('staff'))
    else:
        # Check if the user exists in the users table
        user = c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (email, password)).fetchone()

        if user:
            session['email'] = user[0]
            session['is_staff'] = user[7]

            now = datetime.now()
            ip = request.remote_addr
            c.execute("UPDATE users SET last_login = ?, last_login_ip = ?, successful_logins = successful_logins + 1, \
                       login_attempts = 0 WHERE username = ?", (now.strftime("%Y-%m-%d %H:%M:%S"), ip, email))
            conn.commit()
            conn.close()

            if user[7]:
                return redirect(url_for('staff'))
            else:
                return redirect(url_for('home'))
        else:
            session.pop('email', None)
            session.pop('is_staff', None)

            # Check if the user exists in the staff table
            user = c.execute("SELECT * FROM Staff WHERE email = ?", (email,)).fetchone()
            if user:
                c.execute("UPDATE users SET login_attempts = login_attempts + 1, failed_logins = failed_logins + 1 \
                           WHERE email = ?", (email,))
                if user[5] + 1 >= 5:
                    return redirect(url_for('reset_password', email=email))
            else:
                c.execute("INSERT INTO users (username, password, login_attempts, failed_logins) \
                           VALUES (?, ?, 1, 1)", (email, password))
            conn.commit()
            conn.close()
            app.app_context().push()
            return render_template('index.html', error='Invalid email or password')

@app.route('/home')
def home():
    if 'username' in session and not session['is_staff']:
        username = session['username']
        c.execute("UPDATE users SET successful_logins = successful_logins + 1 WHERE username = ?", (username,))
        conn.commit()
        return render_template('home.html', username=username)
    else:
        return redirect(url_for('index'))

@app.route('/staff')
def staff():
    if 'username' in session and session['is_staff']:
        username = session['username']
        c.execute("UPDATE users SET successful_logins = successful_logins + 1 WHERE username = ?", (username,))
        conn.commit()
        return render_template('staff.html', username=username)
    else:
        return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True, port=8080)