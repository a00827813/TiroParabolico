#José Romero A00827813
#Diego Andrés Moreno A01283790
#Juego Pacman

#importamos librerias que utilizaremos
from random import randrange
from turtle import *
from freegames import vector

#definicion de variables
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Funcion para manejar click en pantalla
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

#Declaracion de variable global, para que el metodo sume infinitamente el tablero del tamaño
#y por lo tanto crear un juego indeterminado
min = -100
max = 100
def inside(xy):
    "Return True if xy within screen."
    global min
    min = min - 100
    global max
    max = max + 100
    return min < xy.x < max and -200 < xy.y < 200

#Desplegar graficos
def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


#Que el tablero avanze junto con el tiro y sus targets
def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.0

    if inside(ball):
        speed.y -= 1.0
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


#Metodos para iniciar el programa y setup
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()