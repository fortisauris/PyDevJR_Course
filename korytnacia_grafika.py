import turtle  # importujeme dalsie prikazy z modulu turtle
# from turtle import *
# from turtle import Turtle

#  NASTAVENIE
t = turtle.Turtle()  # vytvarame objekt Turtle
t.penup()  # zdvihame pero
t.color("red")  # menime farbu pera na cervenu
t.goto(0,0)  # presuvame sa na koordinaty 5,5

# PROGRAM
def nakresli_kolieska(x, y):
    t.goto(x, y)  # chod na zadane koordinaty
    t.pendown()  # pero davame na papier
    for i in range(0,100):  # cyklus for zopakuje prikazy 100x
        t.forward(i)  # tahame dopredu 90 pixelov
        if i > 50:  # ak je i viac ako 50 tak -->
            t.color("orange")  # zmen farbu na oranzovu
        t.left(i)  # otoc dolava o 10 stupnov

nakresli_kolieska(0,0)  # nakresli koliesko na 0,0
nakresli_kolieska(100,100)  # nakresli koliesko na 100, 100
nakresli_kolieska(200,200)  # nakresli koliesko na 200, 200

# TODO PAUZA DO 20:00



# input()  # ocakavame ENTER na klavesnici aby sa program ukoncil
turtle.done()  # zamrazi graficku obrazovku
