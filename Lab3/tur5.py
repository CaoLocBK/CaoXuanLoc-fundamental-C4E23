from turtle import*

def vehsao(x,y,cdai):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(cdai)
        right(144)

mainloop()
