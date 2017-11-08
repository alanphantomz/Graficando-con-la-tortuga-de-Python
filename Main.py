# -*- coding: utf-8 -*-
#!/usr/bin/python3

from turtle import Screen, Turtle
import math
# dimensiones ventana:
ancho = 700
alto = 500

# coordenadas limites:
x1 = -20
y1 = -20
x2 = 20
y2 = 20


def DefinirPantalla(pantalla):
    '''Tamaño, titulo, sistema de coordenadas de la ventana'''
    pantalla.title("Graficador de funciones!!")
    pantalla.setup(ancho, alto)
    pantalla.screensize(ancho - 25, alto - 25)

    # param(x1, y1, x2, y2)
    pantalla.setworldcoordinates(x1, y1, x2, y2)
    pantalla.delay(0) # velocidad

def LeerDominio():
    '''Lee el intervalo de graficación'''
    print("Dominio de la función: ")
    x_ini = float(input("Desde: "))
    x_fin = float(input("Hasta: "))

    # Hay que validar que no sobrepase los limites
    if x_ini < -20: x_ini = -20
    if x_fin > 20: x_fin = 20

    return (x_ini, x_fin)

def RayarCancha(tortuga):
    '''Dibuja los ejes coordenados'''
    tortuga.speed(0)
    tortuga.pencolor("red")
    tortuga.hideturtle()
    tortuga.penup()
    tortuga.goto(x1, 0)
    tortuga.pendown()

    # EJE X
    ini = x1
    while ini <= x2:
        ini += 1
        tortuga.goto(ini, 0)
        tortuga.dot(5)
    tortuga.write("X")

    tortuga.penup()
    tortuga.goto(0, y1)
    tortuga.pendown()

    # EJE Y
    ini = y1
    while ini <= y2:
        ini += 1
        tortuga.goto(0, ini)
        tortuga.dot(5)
    tortuga.write("Y")

def DibujarFuncion(x, x_fin, tortuga):
    y = f(x)
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.pencolor("green")
    tortuga.pensize(1)

    while x <= x_fin:
        x += 0.1
        y = f(x)
        tortuga.goto(x, y)

def f(x):
    y = x * math.sin(x)
    return y

def main():
    pantalla = Screen()
    DefinirPantalla(pantalla)

    # La tortuga se encargará de dibujar
    tortuga = Turtle()
    RayarCancha(tortuga)

    x_ini, x_fin = LeerDominio()

    DibujarFuncion(x_ini, x_fin, tortuga)

    print("Clike la ventana para salir...")
    pantalla.exitonclick()

main()

# TODO: como se haria si se quiere que el usuario ingrese la
# funcion a graficar????