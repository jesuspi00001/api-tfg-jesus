from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/jugador_puntos', methods=['GET', 'POST'])
def jugador_puntos():
    
    return render_template('jugador_puntos.html')


if __name__=="__main__":
    application.run()