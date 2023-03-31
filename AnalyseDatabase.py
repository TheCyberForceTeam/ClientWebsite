import sqlite3
from datetime import datetime
from flask import Flask, request

# create a connection to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

    