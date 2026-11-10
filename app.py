from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/')
def hello_world():
    return 'Hello, World from David Maguire in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://render_lab_postgres_user:M1Hf6Q7wVnEjyobgriSdqZLR0uz9l4bc@dpg-dbpmkmhsrm7s73atppsg-a/render_lab_postgres")
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://render_lab_postgres_user:M1Hf6Q7wVnEjyobgriSdqZLR0uz9l4bc@dpg-dbpmkmhsrm7s73atppsg-a/render_lab_postgres")
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

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://render_lab_postgres_user:M1Hf6Q7wVnEjyobgriSdqZLR0uz9l4bc@dpg-dbpmkmhsrm7s73atppsg-a/render_lab_postgres")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://render_lab_postgres_user:M1Hf6Q7wVnEjyobgriSdqZLR0uz9l4bc@dpg-dbpmkmhsrm7s73atppsg-a/render_lab_postgres")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_str = ""
    response_str += "<table>"
    for player in records:
        response_str += "<tr>"
        for info in player:
            response_str += "<td>{}</td>".format(info)
        response_str += "</tr>"
    response_str += "</table>"
    return response_str

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://render_lab_postgres_user:M1Hf6Q7wVnEjyobgriSdqZLR0uz9l4bc@dpg-dbpmkmhsrm7s73atppsg-a/render_lab_postgres")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully dropped"