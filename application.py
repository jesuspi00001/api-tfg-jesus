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
        resultado = buscar_jugador_puntos(jugador, temporada)
        return render_template('jugador_puntos.html', resultado=resultado[0], flag=resultado[1], total_points=resultado[2])
    
    return render_template('jugador_puntos.html')


@application.route('/jugador_asistencias', methods=['GET', 'POST'])
def jugador_asistencias():
    
    if request.method == 'POST':
        jugador = request.form['jugador']
        temporada = request.form['temporada']
        resultado = buscar_jugador_asistencias(jugador, temporada)
        return render_template('jugador_asistencias.html', resultado=resultado[0], flag=resultado[1], total_asistencias=resultado[2])
    
    return render_template('jugador_asistencias.html')


@application.route('/jugador_rebotes', methods=['GET', 'POST'])
def jugador_rebotes():
    
    if request.method == 'POST':
        jugador = request.form['jugador']
        temporada = request.form['temporada']
        resultado = buscar_jugador_rebotes(jugador, temporada)
        return render_template('jugador_rebotes.html', resultado=resultado[0], flag=resultado[1], total_rebotes=resultado[2])
    
    return render_template('jugador_rebotes.html')


@application.route('/victorias_equipo', methods=['GET', 'POST'])
def victorias_equipo():
    
    if request.method == 'POST':
        equipo = request.form['equipo']
        temporada = request.form['temporada']
        resultado = obtener_victorias_equipo_temporada(equipo, temporada)
        return render_template('victorias_equipo.html', resultado=resultado[0], flag=resultado[1], total_wins=resultado[2])
    
    return render_template('victorias_equipo.html')
    
 

@application.route('/info_api')
def info_api():
    return render_template('info_api.html')



## Funcion busqueda de PUNTOS x jugador en x temporada
def buscar_jugador_puntos(jugador, temporada):
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
        temporada_post = int(temporada) + 1
        temporada_post = str(temporada_post)
        return ["El jugador " + jugador + " tiene una media de " + str(total_points) + " puntos en la temporada " + temporada + "/" + temporada_post + ".", True, str(total_points)]


## Funcion busqueda de ASISTENCIAS x jugador en x temporada
def buscar_jugador_asistencias(jugador, temporada):
    total_asistencias=-1
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
        return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_asistencias)]

    response = conn.getresponse()
    
    if jugador != "" and temporada != "":

        data = json.loads(response.read().decode())
        if data["data"]:
            player_id = data["data"][0]["id"]

            jugador = data["data"][0]["first_name"] + " " + data["data"][0]["last_name"]

            endpoint = f"/api/v1/season_averages?season={temporada}&player_ids[]={player_id}"
            conn.request("GET", endpoint, headers=headers)
            response = conn.getresponse()
            try:
                data = json.loads(response.read().decode())
            except:
                return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_asistencias)]

            conn.close()

            if data["data"]:
                total_asistencias = data["data"][0]["ast"]

        else:
            conn.close()
            return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_asistencias)]
    else:
        return ["Falta por introducir algún parámetro. Recuerda que debes escribir un jugador que perteneciera a la liga en la temporada que selecciones.", False, str(total_asistencias)]

    if total_asistencias == -1:
        return [jugador + " no jugó durante la temporada introducida en la NBA. Introduce una temporada en la que " + jugador + " formara parte de la liga.", False,str(total_asistencias)]
    else:
        temporada_post = int(temporada) + 1
        temporada_post = str(temporada_post)
        return ["El jugador " + jugador + " repartió una media de " + str(total_asistencias) + " asistencias en la temporada " + temporada + "/" + temporada_post + ".", True, str(total_asistencias)]


## Funcion busqueda de REBOTES x jugador en x temporada
def buscar_jugador_rebotes(jugador, temporada):
    total_rebotes=-1
    total_rebotes_ofensivos=-1
    total_rebotes_defensivos=-1
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
        return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_rebotes)]

    response = conn.getresponse()
    
    if jugador != "" and temporada != "":

        data = json.loads(response.read().decode())
        if data["data"]:
            player_id = data["data"][0]["id"]

            jugador = data["data"][0]["first_name"] + " " + data["data"][0]["last_name"]

            endpoint = f"/api/v1/season_averages?season={temporada}&player_ids[]={player_id}"
            conn.request("GET", endpoint, headers=headers)
            response = conn.getresponse()
            try:
                data = json.loads(response.read().decode())
            except:
                return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_rebotes)]

            conn.close()

            if data["data"]:
                total_rebotes = data["data"][0]["reb"]
                total_rebotes_defensivos = data["data"][0]["dreb"]
                total_rebotes_ofensivos = data["data"][0]["oreb"]

        else:
            conn.close()
            return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de jugador válido y una temporada comprendida entre 1946-actual.", False, str(total_rebotes)]
    else:
        return ["Falta por introducir algún parámetro. Recuerda que debes escribir un jugador que perteneciera a la liga en la temporada que selecciones.", False, str(total_rebotes)]

    if total_rebotes == -1:
        return [jugador + " no jugó durante la temporada introducida en la NBA. Introduce una temporada en la que " + jugador + " formara parte de la liga.", False,str(total_rebotes)]
    else:
        temporada_post = int(temporada) + 1
        temporada_post = str(temporada_post)
        return ["El jugador " + jugador + " capturó una media de " + str(total_rebotes) + " rebotes en la temporada " + temporada + "/" + temporada_post + ". De los cuales " + str(total_rebotes_defensivos) + " rebotes defensivos y " + str(total_rebotes_ofensivos) + " rebotes ofensivos.", True, str(total_rebotes)]



def obtener_id_equipo(nombre_equipo):
    nombre_completo_equipo = nombre_equipo
    base_url = "www.balldontlie.io"
    context = ssl._create_unverified_context()

    conn = http.client.HTTPSConnection(base_url, context=context)
    # Realizar solicitud GET a la API para buscar el equipo por nombre
    url_equipo = f"/api/v1/teams?search={nombre_equipo}"
    url_equipo = url_equipo.replace(' ', '%20')
    conn.request("GET", url_equipo)
    res = conn.getresponse()
    data = res.read().decode("utf-8")

    # Analizar la respuesta JSON
    datos_json = json.loads(data)

    # Obtener el ID del equipo si se encuentra en los resultados
    equipo_id = None
    if datos_json['data']:
        for equipo in datos_json['data']:
            if nombre_equipo.upper() == equipo['full_name'].upper() or nombre_equipo.upper() == equipo['name'].upper():
                equipo_id = equipo['id']
                nombre_completo_equipo = equipo['full_name']

    return equipo_id, nombre_completo_equipo




## Funcion busqueda de victorias x equipo en x temporada
def obtener_victorias_equipo_temporada(nombre_equipo, temporada):
    victorias = 0
    equipo_id, nombre_equipo = obtener_id_equipo(nombre_equipo)

    base_url = "www.balldontlie.io"

    context = ssl._create_unverified_context()

    conn = http.client.HTTPSConnection(base_url, context=context)
    headers = {'Content-type': 'application/json'}

    try:
        # Realizar solicitud GET a la API para obtener los datos del equipo y la temporada
        conn.request("GET", f"/api/v1/games?seasons[]={temporada}&team_ids[]={equipo_id}", headers=headers)
        response = conn.getresponse()
    except:
        return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de equipo válido y una temporada comprendida entre 1946-actual.", False, str(victorias)]
    
    try:
        if nombre_equipo != "" and temporada != "":

            data = json.loads(response.read().decode())
            for juego in data["data"]:
                if juego['home_team']['id'] == equipo_id:
                    if juego['home_team_score'] > juego['visitor_team_score']:
                        victorias += 1
                elif juego['visitor_team']['id'] == equipo_id:
                    if juego['visitor_team_score'] > juego['home_team_score']:
                        victorias += 1
        else:
            return ["Falta por introducir algún parámetro. Recuerda que debes escribir un equipo que perteneciera a la liga en la temporada que selecciones.", False, str(victorias)]
    except:
        return ["Alguno de los parámetros introducidos no es correcto. Escribe un nombre de equipo válido y una temporada comprendida entre 1946-actual.", False, str(victorias)]

    if victorias == 0:
        return [nombre_equipo + " no pertenecía a la liga en la temporada seleccionada. Introduce una temporada en la que " + nombre_equipo + " fuera uno de los equipos participantes en esta liga.", False,str(victorias)]
    else:   
        temporada_post = int(temporada) + 1
        temporada_post = str(temporada_post)
        return ["Tenemos registros de que el equipo " + nombre_equipo + " ganó " + str(victorias) + " partidos en la temporada " + temporada + "/" + temporada_post + ".", True, str(victorias)]



if __name__=="__main__":
    application.run()