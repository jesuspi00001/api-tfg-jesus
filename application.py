from flask import Flask, render_template, request
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/jugador_puntos', methods=['GET', 'POST'])
def jugador_puntos():
    if request.method == 'POST':
        jugador = request.form['jugador']
        temporada = request.form['temporada']
        resultado = buscar_jugador(jugador, temporada)
        return render_template('jugador_puntos.html', resultado=resultado[0], flag=resultado[1])
    
    return render_template('jugador_puntos.html')


## Funcion busqueda de puntos x jugador en x temporada
def buscar_jugador(jugador, temporada):

    if jugador == 'Andrea':
        return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada entre 1946-actual.", False]
    else:
        return ["El jugador " + jugador + " tiene una media de tropecientos puntos en la temporada del año " + temporada + ".", True]


if __name__=="__main__":
    application.run()