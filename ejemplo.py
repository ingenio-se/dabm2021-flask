from flask import Flask, render_template,request
import os
import random
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/datos')
def datos():
    user = { 'nombre' : 'david'}
    return render_template('datos.html',title='Titulo personalizado',user=user)

@app.route('/validar',methods=["POST"])
def validar():
    if request.method=="POST":
        usuario = request.form['usuario']
        password = request.form['password']

        resultado=verificar(usuario,password)
        return render_template('menu.html',title='Sistema DABM')

@app.route('/monitor')
def monitor():
    #consultar archivo de parametors
    datos = getDatos()
    #print(datos)
    #obtener lectura
    lectura = random.randint(0,45)
    #enviar a la interfaz

    color=0
    if lectura >= int(datos[0][1]) and lectura <= int(datos[0][2]):
        color=1
    if lectura >= int(datos[1][1]) and lectura <= int(datos[1][2]):
        color=2
    if lectura >= int(datos[2][1]) and lectura <= int(datos[2][2]):
        color=3

    return render_template("monitor.html",datos = datos, lectura=lectura, color=color)

@app.route("/config")
def config():
    return render_template("config.html")

def getDatos():
    directorio = os.path.dirname(__file__)
    nombreArchivo = "bd/parametros.csv"
    ruta = os.path.join(directorio,nombreArchivo)

    f = open(ruta,"r")
    lineas = f.readlines()
    f.close()
    datos=[]
    for l in lineas:
        l = l.replace("\n","")
        l = l.split(";")
        datos.append(l)
    return datos

def verificar(usuario,password):
    #usuario no existe, constraseña correcta, bienvenido
    return True

if __name__ == "__main__":
    app.run(debug=True)