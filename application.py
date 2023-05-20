from flask import Flask, render_template

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    title = 'BasketApp'
    image_url = 'static/imagen2.jpg'
    description = '¿Qué vamos a encontrar aquí? Con esta aplicación podrás obtener datos de diferente índole sobre la liga de balocensto profesional americana, que aglutina los mejores jugadores del mundo.'
    return render_template('index.html', title=title, image_url=image_url, description=description)

if __name__=="__main__":
    application.run()