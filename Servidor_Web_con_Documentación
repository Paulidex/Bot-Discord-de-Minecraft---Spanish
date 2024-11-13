from flask import Flask  # Importa Flask, un marco de trabajo para crear aplicaciones web de forma simple y rápida.

from threading import Thread  # Importa Thread de threading para ejecutar funciones en paralelo sin bloquear la ejecución del programa.

# Inicializa una instancia de la aplicación Flask.
# Flask toma el nombre del módulo actual como argumento, que en este caso es una cadena vacía ('').
# Esto le permite a Flask saber dónde encontrar archivos y recursos relacionados con la aplicación.
app = Flask('')

# Define la ruta raíz de la aplicación web.
# @app.route('/') es un decorador que especifica que la función `home` se ejecutará
# cuando se acceda a la URL raíz (/) del servidor. Esto configura un punto de acceso a la aplicación.
@app.route('/')
def home():
    # La función `home` responde con el texto "I'm alive" cuando la URL raíz es solicitada.
    # Esto indica que el servidor está funcionando correctamente.
    return "I'm alive"

# Define una función `run` que iniciará el servidor Flask cuando se llame.
# Esta función configura el servidor para que sea accesible públicamente en la red.
def run():
    # `app.run` inicia el servidor Flask con las siguientes configuraciones:
    # - host='0.0.0.0' permite el acceso público al servidor en la red, lo que es ideal para aplicaciones que necesitan ser monitoreadas externamente.
    # - port=8080 establece el puerto en el que el servidor escuchará las solicitudes entrantes.
    app.run(host='0.0.0.0', port=8080)

# Define una función `keep_alive` que mantiene el servidor web en funcionamiento en segundo plano.
# Esto es útil para bots o servicios que necesitan un servidor en funcionamiento continuo sin bloquear el flujo principal del programa.
def keep_alive():
    # Crea y lanza un nuevo hilo que ejecutará la función `run` de forma independiente.
    # `Thread(target=run)` crea un hilo que ejecutará la función `run`.
    # `t.start()` inicia el hilo, ejecutando el servidor Flask en segundo plano.
    t = Thread(target=run)
    t.start()
