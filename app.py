from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os

app= Flask(__name__)
app.secret_key="Eddy1987"

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema_py'
mysql.init_app(app)

CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
   return send_from_directory(app.config['CARPETA'],nombreFoto)

#INDEX
@app.route('/')
def index():

    sql = "SELECT * FROM empleado"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    empleados= cursor.fetchall()
    # print(empleados)
    conn.commit()
    return render_template('empleados/index.html',empleados=empleados)

#EDIT
@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleado WHERE id=%s",id)
    empleados = cursor.fetchall()
    conn.commit()
    return render_template('empleados/edit.html',empleados=empleados)

#UPDATE
@app.route('/update',methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    id=request.form['txtId']
    sql = "UPDATE empleado SET nombre=%s, correo=%s WHERE id =%s;"
    datos=(_nombre,_correo,id)
    conn = mysql.connect()
    cursor = conn.cursor()
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
        cursor.execute("SELECT foto FROM empleado WHERE id=%s",id)
        fila = cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE empleado SET foto=%s WHERE id =%s;",{nuevoNombreFoto,id})
        conn.commit()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

#DESTROY
@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT foto FROM empleado WHERE id=%s",id)
    fila = cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
    cursor.execute("DELETE FROM empleado WHERE id=%s",{id})
    conn.commit()
    return redirect('/')

#CREATE
@app.route('/create')
def create():
   return render_template('empleados/create.html')

#STORE
@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    if _nombre=='' or _correo=='' or _foto=='':
        flash('Recuerda llenar los datos de los campos')
        return redirect(url_for('create'))
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
    sql = "INSERT INTO `empleado` (`id`, `nombre`, `correo`, `foto`) VALUES ('', %s, %s, %s)"
    datos=(_nombre,_correo,nuevoNombreFoto)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)