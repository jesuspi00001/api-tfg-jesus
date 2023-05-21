from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    title = 'Inicio'
    image_url = 'static/imagen.jpg'
    description = '¿Qué vamos a encontrar aquí? Con esta aplicación podrás obtener datos de diferente índole sobre la liga de balocensto profesional americana, que aglutina los mejores jugadores del mundo.'
    return render_template('index.html', title=title, image_url=image_url, description=description)

@application.route('/busqueda')
def busqueda():
    title = 'Búsqueda de estadísticas de la NBA'
    image_url = 'static/imagen.jpg'
    description = 'Vista dónde pondremos las busquedas a la base de datos SportsDataBase API.'
    return render_template('busqueda.html', title=title, image_url=image_url, description=description)

@application.route('/quienes_somos')
def quienes_somos():
    title = '¿Quién soy?'
    image_url = 'static/imagen.jpg'
    description = 'Posible vista con una presentación mía. Soy Jesús Pereira Ibáñez, alumnos de Ingeniería Informática blablabla'
    return render_template('quienes_somos.html', title=title, image_url=image_url, description=description)


if __name__=="__main__":
    application.run()