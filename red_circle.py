import turtle

def clic(x, y):
	if x > (button_start.xcor() - 75) and x < (button_start.xcor() + 75):
		if y > (button_start.ycor() - 25) and y < (button_start.ycor() + 25):
			button_start.clear()
			red_circle = turtle.Turtle()
			red_circle.shape('circle')
			red_circle.shapesize(7)
			red_circle.color('red')

	if (попал):
		закрыть		

button_exit = turtle.Turtle()
button_exit.ht()
button_exit.up()
button_exit.setposition(-200, -200)
button_exit.down()
button_exit.forward(100)
button_exit.left(90)
button_exit.forward(50)
button_exit.left(90)
button_exit.forward(100)
button_exit.left(90)
button_exit.forward(50)
button_exit.left(90)

button_exit.up()
button_exit.setposition(-185, -195)
button_exit.write('EXIT', font = ('Arial', 24, 'normal'))

button_start = turtle.Turtle()
button_start.ht()
button_start.up()
button_start.setposition(-75, 0)
button_start.down()
button_start.begin_fill()
button_start.forward(150)
button_start.left(90)
button_start.forward(50)
button_start.left(90)
button_start.forward(150)
button_start.left(90)
button_start.forward(50)
button_start.left(90)
button_start.color('lightgrey')
button_start.end_fill()

button_start.color('black')
button_start.up()
button_start.setposition(-50, 5)
button_start.write('START', font = ('Arial', 24, 'normal'))
button_start.setposition(0, 0)

turtle.listen()
turtle.onscreenclick(clic, 1)


turtle.done()