from flask import Flask, render_template, request, redirect, url_for, session
from db_connection import get_db_connection
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = 'mi_secreto'  # Cambia esto por un valor seguro


@app.route('/')
def home():
    return redirect(url_for('Dashboard_novillito'))

# Ruta para el dashboard
@app.route('/Dashboard_novillito')
def Dashboard_novillito():
    return render_template('Dashboard_novillito.html')

# Ruta para el dashboard
@app.route('/Dashboard_novillo')
def Dashboard_novillo():
    return render_template('Dashboard_novillo.html')

@app.route('/Dashboard_ternero')
def Dashboard_ternero():
    return render_template('Dashboard_ternero.html')

@app.route('/Dashboard_toro')
def Dashboard_toro():
    return render_template('Dashboard_toro.html')

@app.route('/Dashboard_vaca')
def Dashboard_vaca():
    return render_template('Dashboard_vaca.html')

# Ruta para registro de usuario
@app.route('/subscribirse', methods=['GET', 'POST'])
def subscribirse():
    if request.method == 'POST':
        username = request.form['username']
        lastname = request.form['lastname']
        correo = request.form['correo']
        cel = request.form['cel']
        horario_llamada = request.form['horario_llamada']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insertar usuario en la base de datos
        query = "INSERT INTO users (username, lastname,correo,cel,horario_llamada) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (username,lastname,correo,cel,horario_llamada))
            conn.commit()
            cursor.close()
            conn.close()
            return render_template('Dashboard_novillito.html')
        except mysql.connector.Error as err:
            return f"Error: {err}"

    return render_template('subscribirse.html')

if __name__ == '__main__':
    app.run(debug=True)
