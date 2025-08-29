import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test"
)
cursor = conn.cursor()
cursor.execute('CREATE DATABASE busapp1')