import turtle
import random

screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
p = turtle.Turtle()

shape=int(input("How many sides should the shape have:"))
colors=["Blue","red","green","pink","yellow","orange"]

random_index=random.randint(0,len(colors)-1)

def make_shape (clr):
  p.color(clr)
  p.begin_fill()
  shape_turn=360/shape
  for i in range(shape):
    p.forward(40)
    p.left(shape_turn)
  p.end_fill()

make_shape(colors[random_index])
turtle.done()