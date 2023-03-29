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
                last_login_date text, address text, phone text, is_staff boolean)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Admin
                (email text, username text, password text, successful_logins integer,
                unsuccessful_logins integer, total_login_attempts integer, last_login_ip_address text,
                last_login_date text, address text, phone text, is_staff boolean)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Users
                (email text, username text, password text, successful_logins integer,
                unsuccessful_logins integer, total_login_attempts integer, last_login_ip_address text,
                last_login_date text, address text, phone text, is_staff boolean)''')

# insert data into the tables
staff_data = ('Staff@ncsc.com', 'Staff', 'SuperSecretPassword', 0, 0, 0, 'Hard-Coded', 'Hard-Coded','The Cyber Force Team HQ', '0123456789', 1)
admin_data = ('Admin@ncsc.com', 'Admin', 'SuperSecretPassword2', 0, 0, 0, 'Hard-Coded', 'Hard-Coded','The Cyber Force Team HQ', '0123456789', 1)
user_data = ('user@ncsc.com', 'User', 'Password', 0, 0, 0, 'Hard-Coded', 'Hard-Coded','The Cyber Force Team HQ', '0123456789', 0)

cur.execute('INSERT INTO Staff VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', staff_data)
cur.execute('INSERT INTO Admin VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', admin_data)
cur.execute('INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user_data)

# commit the changes and close the connection
conn.commit()
conn.close()
