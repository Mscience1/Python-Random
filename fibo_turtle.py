import turtle


win = turtle.Screen()
win.title("Golden Spiral")


tim = turtle.Turtle()
square_draw = turtle.Turtle()

def fibo_seq(n):
    list = [1]
    for x in range(0,n,1):
        numb =  list[x] + list[x-1]
        list.append(numb)
        tim.forward(numb)
        tim.left(45)
        tim.forward(numb)
        tim.left(45)
        square_draw.forward(numb)
        square_draw.left(90)
        square_draw.forward(numb)
        square_draw.left(90)

    del list[1]
    print(list)

fibo_seq(100)

win.listen()
win.mainloop()



