import mysql.connector
import pymysql
config={
    "user":"root",
    "password":"root",
    "host":"127.0.0.1",
    "port":3306,
    "database":"student_db"
}

# connection object
connection=pymysql.connect(**config)
def get_connection():
    return connection
# .\.venv\Scripts\activate
