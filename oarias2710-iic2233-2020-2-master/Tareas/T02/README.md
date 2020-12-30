# Tarea 02

## Descripción general del código

No alcancé a completar la tarea. El código que completé logra implementar la ventana de inicio, la ventana de ranking y la ventana de juego. La ventana de juego está diseñada pero no completa. No logré ejecutar el juego, tampoco lograr el *drag and drop* de los pingüinos. Las flechas logré ponerlas en posición, pero nada de su mecánica interna. Se incluye la música (las dos canciones) y las flechas en el caso de juego principiante.

## Ejecución

Debe ejecutarse el archivo `main.py` en una carpeta en donde también estén los archivos `parametros.py` (parámetros del juego), `funciones.py` (funciones que se usan en la ejecución) y `clases_auxiliares.py` (clases adicionales usadas). Además en esta carpeta de ejecución deben incluirse las carpetas `songs/` y `sprites/`. Además, deben incluirse en la carpeta los siguientes archivos de *QT Designer*: `v_inicio.ui`, `v_juego.ui`, `v_ranking.ui`, que contienen el diseño de las ventanas.

## Librerías usadas

 - **Librerías externas:** *sys*, *os*, *time*, *PyQt5*, *threading*, *random*.
 - **Librerías propias:** *parametros*, *funciones*, *clases_auxiliares*. 

## Pauta de corrección detallada 
- **Ventana de Inicio:** `main.py`, línea 120, línea 214.
- **Ventana de Ranking:** `main.py`, línea 159, línea 216.
- **Ventana de Juego:**
-- *Generales:* Ver `main.py`, línea 118. Se implementó correctamente el botón Salir, se diferencian correctamente los elementos de la ventana y se ubican correctamente los pingüirines en posición y su precio.
-- *Fase pre Ronda:* Ver `main.py`, línea 118. Se implementan los selectores de dificultad, y canción usando señales.
-- *Fase de Ronda:* Ver `main.py`, línea 118. Se reproduce la canción elegida, y las flechas funcionan en el nivel Principiante. No se capturan las flechas. Las flechas y la canción duran los 30 segundos que corresponden al nivel.
-- *Fase post Ronda:* No implementado.
- **Mecánicas:**
-- *Pingüirín*: Sólo logré poner las imágenes en la ventana de juego, no logré implementar el *drag and drop*.
-- *Flechas*: Implementé el movimiento de las flechas normales, pero no logré hacer la captura de las flechas. Ver `main.py` línea 30, funciones `boton_comenzar_clickeado`, `terminar_principiante` y `creador_de_flechas_principiante`.
- **Funcionalidades extra:** No implementado.
- **Bonus:** No implementado.



## Comentarios finales
Lamento no haber podido terminar, le puse todo el esfuerzo, empecé desde que se subió la tarea a investigar como implementar todo, pero sencillamente no alcancé. Tengo temor de la T03, siento que en esa tarea me la voy a jugar si paso o no el ramo. De todas maneras aprendí bastante, pero llegué destruido al último día; de hecho, subo los archivos finales antes de las 20:00 hrs. porque no tengo más energía para dedicarle a la tarea y tengo que ponerme a trabajar/estudiar en mis otros ramos. Gracias por el apoyo y las correcciones detalladas. 

Saludos.

**Óscar Arias R.** 
oaarias@uc.cl
