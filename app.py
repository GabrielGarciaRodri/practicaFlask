#INICIALIZA FLASK

from flask import Flask, render_template

app = Flask (__name__)


#RUTA DE LAS IMAGENES



#RUTAS
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/views/abrigos")
def abrigos():
    return render_template('/views/abrigos.html')

@app.route("/views/camisetas")
def camisetas():
    return render_template("/views/camisetas.html")

@app.route("/views/pantalones")
def pantalones():
    return render_template("/views/pantalones.html")

@app.route("/views/carrito")
def carrito():
    return render_template("/views/carrito.html")

@app.route("/views/carritoVacio")
def carritoVacio():
    return render_template("carritoVacio.html")

@app.route("/views/carritoLleno")
def carritoLleno():
    return render_template("carritoLleno.html")

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