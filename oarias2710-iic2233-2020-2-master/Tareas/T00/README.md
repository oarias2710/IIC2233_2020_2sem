# Tarea 00: DCCombate Naval :ship: :bomb:

<!-- Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.** -->

## Consideraciones generales :octocat:

Logré implementar todo lo solicitado en la pauta.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Menú de Inicio del programa
    1. El menú de Inicio contiene todas las opciones pedidas en el enunciado. :white_check_mark:
    2. El usuario puede elegir un apodo correctamente con las restricciones estipuladas en el enunciado. :white_check_mark:
    3. Si se ingresa un apodo no válido se informa al usuario, dando la opción de volver a ingresar el apodo o volver al Menú de Inicio. :white_check_mark:
    4. Se puede comenzar una partida nueva, permitiendo al jugador elegir el tamaño del tablero. :white_check_mark:
    5. Si se ingresan dimensiones no válidas se informa al usuario y no se deja avanzar al siguiente menú. :white_check_mark:
    6. Se puede salir del programa de forma correcta. :white_check_mark:
    7. Se muestran los 5 jugadores con los puntajes más altos del archivo puntajes.txt. Los puntajes se encuentran ordenados de mayor a menor. :white_check_mark:

* Flujo del juego
    1. El menú contiene todas las opciones mínimas pedidas en el enunciado. :white_check_mark:
    2. El tablero es generado de forma correcta con el tamaño ingresado anteriormente. :white_check_mark:
    3. Se pueden visualizar los barcos del jugador y del enemigo según la notación pedida. :white_check_mark:
    4. El tablero se actualiza de forma correcta después de cada turno. :white_check_mark:
    5. Al acertar un disparo, se marca la celda y se puede seguir disparando. Esta regla se cumple tanto para el jugador como para el oponente :white_check_mark:
    6. Al errar un tiro se marca en el tablero con una "X" y se pasa al turno del otro jugador. Esta regla se cumple tanto para el jugador como para el oponente :white_check_mark:
    7. Las bombas regulares son implementadas de acuerdo a lo estipulado en el enunciado. :white_check_mark:
    8. Se puede seleccionar una bomba Cruz. La Bomba produce el efecto indicado en el enunciado. Se respeta el radio de explosión. :white_check_mark:
    9. Se puede seleccionar una bomba X. La Bomba produce el efecto indicado en el enunciado. Se respeta el radio de explosión. :white_check_mark:
    10. Se puede seleccionar una bomba Diamante. La Bomba produce el efecto indicado en el enunciado. Se respeta el radio de explosión. :white_check_mark:
    11. No se puede volver a disparar en lugares donde ya se disparó. :white_check_mark:
    12. Los barcos se distribuyen de manera aleatoria en los tableros. :white_check_mark:
    13. Los barcos no se traslapan ni se ubican fuera del tablero. :white_check_mark:
    14. El oponente juega de manera automática siguiendo las mismas reglas que el jugador. :white_check_mark:
    15. Se imprimen en pantalla las coordenadas donde el oponente disparó. Las coordenadas siguen el formato del enunciado. :white_check_mark:

* Término del juego
    1. El juego finaliza si se destruyen todos los barcos de alguno de los jugadores. :white_check_mark:
    2. El juego se acaba cuando el jugador se rinde. :white_check_mark:
    3. El puntaje final se calcula de forma correcta. :white_check_mark:
    4. El puntaje final se calcula y almacena cuando corresponde. :white_check_mark:

* General
    1. Los menús son a prueba de todo tipo de errores.  :white_check_mark: (Eso sí, debo hacer una precisión. De acuerdo a la pauta, sólo cuando se pone mal el nombre se da la opción de poner bien el nombre o vovler al menú de inicio. En los demás input se debe escribir en forma correcta la información, números y letras (en mayúsculas o minúsculas) pero no se da la opción de volver al menú de inicio. Esto porque no aparecía en la pauta, pero el mismo día de la entrega vi que aparecía en una issue que un ayudante hacia extensible eso a todos los inputs. A esa altura ya no lo pude modificar. Pero cumple con lo pedido de que sea a prueba de errores.)
    2. Se utilizan los parámetros entregados dentro del programa, y se importa el módulo de forma correcta.  :white_check_mark:
    3. El programa se encuentra modularizado si es necesario.  :white_check_mark:
    4. El programa respeta correctamente PEP8.  :white_check_mark:

<!-- 
* <Nombre item pauta<sub>1</sub>>: Hecha completa
* <Nombre item pauta<sub>2</sub>>: Me faltó hacer <insertar qué cosa faltó>
    * <Nombre subitem pauta<sub>2.1</sub>>: Hecha completa 
    * <Nombre subitem pauta<sub>2.2</sub>>: Me faltó hacer <insertar qué cosa faltó>
    * ...
* <Nombre item pauta<sub>3</sub>>: Me faltó hacer <insertar qué cosa faltó>
* ...
* <Nombre item pauta<sub>n</sub>>: Me faltó hacer <insertar qué cosa faltó> -->


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```dccombate_naval.py```. Se debe entregar los siguientes archivos que tienen que estar en la misma carpeta en que se ejecuta el módulo principal:
1. ```parametros.py```
2. ```puntajes.txt```
3. ```tablero.py```
4. Además debe estar en la misma carpeta el archivo ```funciones.py``` en donde están las funciones que creépara ejecutar el programa.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: importé la libreria completa.
2. ```os```: importé la libreria completa (aunque finalmente no se usa).

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones```: Contiene las funciones ```puntaje```, ```respuesta_valida```, ```respuesta_valida_letra```, ```lanzar_bomba```, ```lanzar_bomba_regular```, ```dimensiones_tablero```, ```crea_tablero```. 

<!-- ## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md). -->
