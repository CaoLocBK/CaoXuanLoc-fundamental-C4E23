from turtle import*
from random import randint
from tur5 import vehsao


shape("turtle")
speed(0)
color("blue")
for i in range(100):
    x = randint(-300,300)
    y = randint(-300,300)
    cdai = randint(3,10)
    vehsao(x,y,cdai)

mainloop()