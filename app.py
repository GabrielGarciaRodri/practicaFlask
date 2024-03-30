#INICIALIZA FLASK

from flask import Flask, render_template

app = Flask (__name__)


#RUTAS
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacto")
def contacto():
    return "<h1>contacto</h1>"

@app.route("/home")
def home():
    return "HOME!"

@app.route("/hola/<string:nombre>")
def hola(nombre):
    return f"<h1>Hola {nombre}</h1>"


#Con este debuger se actualiza la pag automaticamente 
#No es necesario reiniciar el servidor
if __name__ == "__main__":
    app.run (debug=True)