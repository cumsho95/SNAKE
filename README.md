# TODO
-Crear el cuerpo de la culebra.
-Mover la culebra.
-Controlar los movimientos de la culebra.
-Detectar  la colision con la comida.
-Manejar el puntaje.
-Detectar la colision con los muros.
-Detectar cuando colisione con sigo mismo.

## Crear el cuerpo de la culebra

Primero importamos (turtle) y de este importamos el screen para el tablero y turtle para la culebra.

Creando el tablero cuadrado de 600*600 de color NEGRO, con tutilo juego de la culebra(Snake Game), 
    Screen = Screen()
    Screen.setup(width=600, height=600)
    Screen.bgcolor("black")
    Screen.title("Snake Game")

Para que la ventana que se abra y no se cierre de inmediato se pone:
    Screen.exitonclick()

Crear el cuerpo en 3 cuadrados blancos especificando las coordenadas de cada cuadrado para fomar el cuerpo de la culebra:

    segment_1 = Turtle("square")
    segment_1.color("white")

    segment_2 = Turtle("square")
    segment_2.color("white")
    segment_2.goto(-20, 0)

    segment_3 = Turtle("square")
    segment_3.color("white")
    segment_3.goto(-40, 0)

Y todo esto de fomra remasterizada sería:
    starting_positions = [(0, 0),(-20, 0),(-40, 0)]

    for position in starting_positions:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.goto(position)

## Mover la culebra

Primero agregamos los elementos creados para tratar los tres segmentos como uno solo:

    segments.append(new_segment)

Luego le damos la condicion para que se mueva constantemente hacia adelante con un ciclo:

    game_is_on = True

    while game_is_on:
        for seg in segments:
            seg.forward(20)

Para que la línea que queda en el recorrido no se muestre se le agrega un (new_segment.penup()) que significa que dibujer a mano alzada:

    new_segment.penup()

Para poder controlar el tiempo con el que se desplaza la culebra importamos (import time) y retrasamos el tiempo en 1 segundo:

    time.sleep(0.1)

