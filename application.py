from flask import Flask, render_template, request
import requests

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/jugador_puntos', methods=['GET', 'POST'])
def jugador_puntos():
    
    # if request.method == 'POST':
    #     jugador = request.form['jugador']
    #     temporada = request.form['temporada']
    #     resultado = buscar_jugador(jugador, temporada)
    #     return render_template('jugador_puntos.html', resultado=resultado[0], flag=resultado[1])
    
    return render_template('jugador_puntos.html')


## Funcion busqueda de puntos x jugador en x temporada
# def buscar_jugador(jugador, temporada):
#     url_player = f"https://www.balldontlie.io/api/v1/players?search={jugador}"

#     player = requests.get(url_player)
#     points=-1

#     if player.status_code == 200 and jugador!="":
#         data_player = player.json()
#         if data_player['data']:
#             player_id = data_player['data'][0]['id']

#             url_puntos = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}&season={temporada}"
 
#             puntos = requests.get(url_puntos)
            
#             if puntos.status_code == 200:
#                 data_puntos = puntos.json()
#                 if data_puntos['data']:
#                     points = data_puntos['data'][0]['pts']

#         else:
#             return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada entre 1946-actual.", False]
#     else:
#         return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada entre 1946-actual.", False]

#     if points == -1:
#         return [jugador + " no jugó durante la temporada introducida en la NBA. Introduce una temporada en la que " + jugador + " formara parte de la liga.", False]
#     else:
#         return ["El jugador " + jugador + " tiene una media de: " + str(points) + " puntos en la temporada del año " + temporada + ".", True]


if __name__=="__main__":
    application.run()