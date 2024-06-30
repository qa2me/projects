import turtle


t = turtle.Turtle()
t.speed(10)  
x=144
qais=['blue','red','gray','yellow','green','black']
t.color("blue")
t.begin_fill()
for i in range(180):
  t.color(qais[i%6])
  for _ in range(5):
      t.forward(200)  
      t.right(x+2)  
    


t.hideturtle()