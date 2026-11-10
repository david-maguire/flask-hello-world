from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://render_lab_postgres_user:M1Hf6Q7wVnEjyobgriSdqZLR0uz9l4bc@dpg-dbpmkmhsrm7s73atppsg-a/render_lab_postgres")
    conn.close()
    return "Database connection successful"