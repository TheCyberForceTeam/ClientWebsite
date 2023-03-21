import sqlite3
from datetime import datetime
import os
from flask import Flask, request, redirect, render_template, session, url_for

secret_key = os.urandom(24).hex()
print(secret_key)

app = Flask(__name__,static_folder='static', template_folder='/Users/nathanbrown-bennett/Programming/Web Server/ClientWebsite/')
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
conn.commit()

@app.route('/', methods=['GET', 'POST'])
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
        session['email'] = user[1]
        session['is_staff'] = True

        now = datetime.now()
        ip = request.remote_addr
        c.execute("UPDATE Staff SET last_login = ?, last_login_ip = ?, successful_logins = successful_logins + 1, \
                   total_login_attempts = 0 WHERE email = ?", (now.strftime("%Y-%m-%d %H:%M:%S"), ip, email))
        conn.commit()
        conn.close()

        return redirect(url_for('staff'))
    else:
        # Check if the user exists in the users table
        user = c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (email, password)).fetchone()

        if user:
            session['email'] = user[0]  # should be user[1] since email is the second column in the table
            session['is_staff'] = user[7]

            now = datetime.now()
            ip = request.remote_addr
            c.execute("UPDATE users SET last_login = ?, last_login_ip = ?, successful_logins = successful_logins + 1, \
                       total_login_attempts = 0 WHERE username = ?", (now.strftime("%Y-%m-%d %H:%M:%S"), ip, email))
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
                c.execute("UPDATE Staff SET total_login_attempts = total_login_attempts + 1, unsuccessful_logins = unsuccessful_logins + 1 \
                           WHERE email = ?", (email,))
                if user[5] + 1 >= 5:
                    return redirect(url_for('reset_password', email=email))
            else:
                c.execute("INSERT INTO users (username, password, total_login_attempts, unsuccessful_logins) \
                           VALUES (?, ?, 1, 1)", (email, password))
            conn.commit()
            conn.close()

            return render_template('index', error='Invalid email or password')

@app.route('/home')
def home():
    if 'username' in session and not session['is_staff']:
        username = session['username']
        c.execute("UPDATE users SET successful_logins = successful_logins + 1 WHERE username = ?", (username,))
        conn.commit()
        return render_template('index.html', username=username)
    else:
        return redirect(url_for('index.html'))

@app.route('/staff')
def staff():
    if 'username' in session and session['is_staff']:
        username = session['username']
        c.execute("UPDATE users SET successful_logins = successful_logins + 1 WHERE username = ?", (username,))
        conn.commit()
        return render_template('staff.html', username=username)
    else:
        return redirect(url_for('index.html'))
if __name__ == '__main__':
    app.run(debug=True, port=8080)