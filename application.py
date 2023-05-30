from flask import Flask, render_template, request
import http.client
import json
import ssl

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
        return render_template('jugador_puntos.html', resultado=resultado[0], flag=resultado[1], total_points=resultado[2])
    
    return render_template('jugador_puntos.html')


## Funcion busqueda de puntos x jugador en x temporada
def buscar_jugador(jugador, temporada):
    total_points=-1
    base_url = "www.balldontlie.io"
    endpoint = "/api/v1/players"

    context = ssl._create_unverified_context()

    conn = http.client.HTTPSConnection(base_url, context=context)
    headers = {'Content-type': 'application/json'}

    params = f"search={jugador}"
    url_player = f"{endpoint}?{params}"
    url_player = url_player.replace(' ', '%20')
    try:
        conn.request("GET", url_player, headers=headers)
    except:
        return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_points)]

    response = conn.getresponse()
    
    if jugador != "" and temporada != "":

        data = json.loads(response.read().decode())
        if data["data"]:
            player_id = data["data"][0]["id"]

            jugador = data["data"][0]["first_name"] + " " + data["data"][0]["last_name"]
            equipo = data["data"][0]["team"]["full_name"]

            endpoint = f"/api/v1/season_averages?season={temporada}&player_ids[]={player_id}"
            conn.request("GET", endpoint, headers=headers)
            response = conn.getresponse()
            try:
                data = json.loads(response.read().decode())
            except:
                return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_points)]


            conn.close()

            if data["data"]:
                total_points = data["data"][0]["pts"]

        else:
            conn.close()
            return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_points)]
    else:
        return ["Falta por introducir algún parámetro. Recuerda que debes escribir un jugador que perteneciera a la liga en la temporada que selecciones.", False, str(total_points)]

    if total_points == -1:
        return [jugador + " no jugó durante la temporada introducida en la NBA. Introduce una temporada en la que " + jugador + " formara parte de la liga.", False,str(total_points)]
    else:
        return ["El jugador " + jugador + " tiene una media de: " + str(total_points) + " puntos en la temporada del año " + temporada + ".", True, str(total_points)]


if __name__=="__main__":
    application.run()