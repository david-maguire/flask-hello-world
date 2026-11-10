from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://render_lab_postgres_user:M1Hf6Q7wVnEjyobgriSdqZLR0uz9l4bc@dpg-dbpmkmhsrm7s73atppsg-a/render_lab_postgres")
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def creating():
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return "Table 'Basketball' successfully created"
    