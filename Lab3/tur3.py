from turtle import*

def draw_square(cdai, maus):
    for i in range(4):
        color(maus)
        forward(cdai)
        left(90)
draw_square(100,"orange")