# Tarea 03

## Descripción general del código

Estuve muy lejos de completar la tarea. Me centré en hacer que el grafo tuviera las funcionalidades requeridas y traté de avanzar en la parte de networking, pero sólo alcancé a usar las clases y métodos que vimos en los ejemplos de los contenidos de la semana-14.

## Ejecución

Debe ejecutarse el archivo `main.py`  en la carpeta `server/`  y el `main.py` en la carpeta `client/`. Además, cada una de estas carpetas debe tener su respectivo archivo `networking.py` y `parametros.json`. Finalmente, el archivo `grafo.json` debe estar en la carpeta `client/`.

## Librerías usadas

- **Librerías externas: *json*, *random*, *faker*, *socket*.
- **Librerías propias: *networking* (las clases y métodos de la semana 14).

## Pauta de corrección detallada

- **Networking:**  `client/networking.py` y `server/networking.py`. Ver también `client/main.py` (línea 8) y `server/main.py` (línea 374). Usé el protocolo TCP/IP e instancié y conecté los sockets. Pero no hice lo relacionado con conexión y manejo de clientes.
- **Arquitectura Cliente - Servidor:** No implementado.
- **Manejo de bytes:** No implementado.
- **Interfaz gráfica:** No implementado.
- **Grafo:** Está implementado en el archivo `server/main.py`. Ahí creé las clases `Mapa`, `Camino`, `Nodo`, `Hexagono` y `Jugador`, que con sus respectivos métodos generan el mapa y realizan la mayoría de las operaciones. Se instancia correctamente un grafo no dirigido y el grafo se actualiza de acuerdo a las acciones usando los métodos de la clase `Mapa`. Se verifica que se cumplen las condiciones para la construcción de chozas y carreteras. No alcancé a implementar un método para calcular la carretera más larga.
- **Reglas del DCColonos:** Está implementado en el archivo `server/main.py`. Se asigna correctamente a cada hexágono una materia prima y un número de ficha al azar. Además se colocan las chozas y carreteras iniciales en posición, y se reparten los recursos iniciales para los jugadores. Además se reparten correctamente los recursos del hexágono para cada jugador, correspondientes al número obtenido (en los dados). En caso que sea 7 el resultado, como mi pauta es diferente, puse una bonificación especial (ver `server/parametros.json`). Existe un método que calcula los puntos para cada jugador al finalizar cada turno. No implementé la bonificación para la carretera más larga pues no generé un método para calcular la carretera más larga.
- **General:** Todos los parámetros están en los archivos `parametros.json` correspondientes. Además se carga el archivo `grafo.json` para construir el grafo.
- **Bonus:** No implementado.

## Comentarios finales

Nuevamente no pude terminar la tarea. Dentro de mis posibilidades le puse todo el tiempo y esfuerzo, y traté de concentrarme en las partes que pudiera terminar. Lo lamento más porque me ofrecieron la posibvilidad de una pauta con menos cosas a implementar, pero no alcancé.

Entiendo que mi nota será muy mala, pero espero que al menos me alcance para pasar el ramo. Me esforcé en las actividades sumativas, así que espero que eso me ayude, junto con las formativas y las autoevaluaciones. Siento que aprendí mucho, y a pesar del cansancio y de tener la cabeza en otro lado, me entretuve trabajando en la Tarea.

Gracias por el apoyo, la comprensión y las correcciones detalladas.

Saludos atentos.

**Óscar Arias R.**
oaarias@uc.cl
