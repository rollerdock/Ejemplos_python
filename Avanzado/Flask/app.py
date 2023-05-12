from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('productos.db')
    return conn

def close_db(conn):
    conn.close()

def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio FLOAT NOT NULL
        )
    ''')
    conn.commit()
    close_db(conn)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        conn = connect_db()
        c = conn.cursor()
        c.execute('INSERT INTO productos (nombre, descripcion, precio) VALUES (?, ?, ?)', (nombre, descripcion, precio))
        conn.commit()
        close_db(conn)
        return redirect(url_for('ver_productos'))
    return render_template('agregar.html')

@app.route('/ver_productos')
def ver_productos():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM productos')
    productos = c.fetchall()
    close_db(conn)
    return render_template('ver_productos.html', productos=productos)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
