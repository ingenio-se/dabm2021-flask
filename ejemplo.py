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

    return render_template("monitor.html",datos = datos, lectura=lectura)


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