pensize(5)
penup()
setposition(-200,200)
#sky function
def sky():
    pendown()
    color("salmon")
    forward(400)
#cloud function
def cloud():
    pendown()
    forward(130)
    downright()
    forward(130)
    downleft()
    penup()
    backward(8)
    pendown()
    forward(150)
    penup()
    downright()
    pendown()
    forward(150)
    penup()
    downleft()
    forward(10)
    pendown()
    forward(150)
    downright()
    forward(150)
    penup()
    downleft()
    penup()
    backward(10)
    pendown()
    forward(150)
    downright()
    forward(150)
#function to move it down one row from the right
def downright():
    right(90)
    forward(4)
    right(90)
#function to move it down from the left
def downleft():
    left(90)
    forward(4)
    left(90)
#ocean function
def ocean():
    pendown()
    color("teal")
    forward(400)
#sun function
def sun():
    color("gold")
    begin_fill()
    left(90)
    circle(50,180)
    end_fill()
speed(0)
# makes the sky with function
for i in range(29):
    sky()
    downright()
    sky()
    downleft()
penup()
# makes the ocean with function
setposition(-200,-30)
for i in range(25):
    ocean()
    downright()
    ocean()
    downleft()
penup()
setposition(-183,-60)
# functions make reflections
def reflections():
    pendown()
    color("pale turquoise")
    forward(90)
def reflection():
    reflections()
    penup()
    backward(30)
    right(90)
    forward(35)
    left(90)
    pendown()
    reflections()
    penup()
    right(90)
    forward(35)
    left(90)
    backward(189)
    pendown()
    reflections()
    penup()
    setposition(-148,-170)
    pendown()
    reflections()
    penup()
# makes the ocean wave reflections
pensize(4)
reflection()
penup()
setposition(18,-70)
pendown()
reflection()
penup()
setposition(80,-170)
pendown()
reflections()
penup()
setposition(165,-40)
pendown()
reflections()
penup()
setposition(40,-25)
pendown()
pensize(5)
# makes the sun on horizon with function
sun()
left(90)
forward(100)
# make the clouds and the sun reflections now 
# makes sun reflections on ocean 
penup()
setposition(-60,-27)
pendown()
color ("orange")
forward(100)
penup()
setposition(-55,-30)
pendown()
forward(90)
downright()
forward(90)
penup()
downleft()
forward(5)
pendown()
forward(80)
downright()
forward(80)
penup()
downleft()
forward(5)
pendown()
forward(70)
downright()
forward(70)
penup()
downleft()
forward(5)
pendown()
forward(70)
penup()
downright()
forward(2)
pendown()
forward(77)
penup()
downleft()
forward(10)
pendown()
forward(60)
downright()
penup()
backward(5)
pendown()
forward(65)
penup()
downleft()
backward(10)
pendown()
forward(78)
downright()
penup()
backward(8)
pendown()
forward(78)
penup()
downleft()
backward(13)
pendown()
forward(76)
#second layers of reflections this time gold
penup()
setposition(-55,-30)
def gold():
    pensize(3)
    pendown()
    color("gold")
    forward(19)
gold()
penup()
forward(7)
downright()
forward(-50)
pendown()
gold()
penup()
downleft()
backward(18)
downright()
pendown()
gold()
penup()
backward(30)
downleft()
pendown()
gold()
penup()
downright()
penup()
forward(47)
downleft()
gold()
penup()
downright()
backward(55)
downleft()
backward(50)
gold()
penup()
downright()
downleft()
backward(59)
gold()
penup()
downright()
downleft()
forward(28)
gold()
pensize(5)
# cloud time
penup()
setposition(-170,160)
color("peach puff")
#function for a cloud :)
def cloud():
    pendown()
    forward(130)
    downright()
    forward(130)
    downleft()
    penup()
    backward(8)
    pendown()
    forward(150)
    penup()
    downright()
    pendown()
    forward(150)
    penup()
    downleft()
    forward(10)
    pendown()
    forward(150)
    downright()
    forward(150)
    penup()
    downleft()
    penup()
    backward(10)
    pendown()
    forward(150)
    downright()
    forward(150)
cloud()
penup()
setposition(158,50)
cloud()
penup()
setposition(-200,-10)
backward(50)
pendown()
forward(130)
downright()
forward(130)
downleft()
penup()
backward(8)
pendown()
forward(150)
penup()
downright()
pendown()
forward(150)
penup()
setposition(140,205)
left(180)
forward(130)
downright()
forward(130)
downleft()
penup()
backward(8)
pendown()
forward(150)
penup()
downright()
pendown()
forward(150)
downleft()
penup()
backward(10)
pendown()
forward(150)
downright()
forward(150)
#cloud details :')
penup()
color("indian red")
pensize(2)
setposition(-171,162)
pendown()
left(180)
forward(133)
right(90)
forward(8)
left(90)
forward(12)
right(90)
forward(8)
left(90)
forward(11)
right(90)
forward(8)
right(90)
forward(11)
left(90)
forward(9)
right(90)
forward(154)
right(90)
forward(10)
right(90)
forward(10)
left(90)
forward(7)
left(90)
forward(10)
right(90)
forward(9)
right(90)
forward(7)
left(90)
forward(8)
penup()
setposition(160,48)
pendown()
forward(8)
right(90)
forward(8)
left(90)
forward(8)
left(90)
forward(10)
right(90)
forward(8)
right(90)
forward(11)
left(90)
forward(8)
left(90)
forward(155)
left(90)
forward(8)
right(90)
forward(11)
left(90)
forward(9)
left(90)
forward(11)
right(90)
forward(8)
left(90)
forward(11)
right(90)
forward(8)
left(90)
forward(134)
color("crimson")
penup()
setposition(-200,-8)
pendown()
forward(83)
right(90)
forward(8)
left(90)
forward(11)
right(90)
forward(8)
right(90)
forward(100)
penup()
setposition(130,200)
backward(90)
pendown()
forward(90)
left(90)
forward(8)
right(90)
forward(10)
left(90)
forward(10)
left(90)
forward(100)