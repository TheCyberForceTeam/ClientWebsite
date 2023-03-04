import sqlite3
from datetime import datetime
from flask import Flask, request

# create a connection to the database
conn = sqlite3.connect('database.db')

# create a cursor object
cur = conn.cursor()

# create the Staff and Admin tables
cur.execute('''CREATE TABLE IF NOT EXISTS Staff
                (email text, username text, password text, successful_logins integer,
                unsuccessful_logins integer, total_login_attempts integer, last_login_ip_address text,
                last_login_date text)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Admin
                (email text, username text, password text, successful_logins integer,
                unsuccessful_logins integer, total_login_attempts integer, last_login_ip_address text,
                last_login_date text)''')

cur.execute('''CREATE TABLE IF NOT EXISTS users
                (username text, password text, email text, last_login text,
                 last_login_ip text, unsuccessful_logins integer,
                 successful_logins integer, total_login_attempts integer)''')


# insert data into the tables
staff_data = ('Staff@coffee.shop', 'Staff', 'SuperSecretPassword', 0, 0, 0, '', '')
admin_data = ('Admin@coffee.shop', 'Admin', 'SuperSecretPassword2', 0, 0, 0, '', '')

cur.execute('INSERT INTO Staff VALUES (?, ?, ?, ?, ?, ?, ?, ?)', staff_data)
cur.execute('INSERT INTO Admin VALUES (?, ?, ?, ?, ?, ?, ?, ?)', admin_data)

# commit the changes and close the connection
conn.commit()
conn.close()
