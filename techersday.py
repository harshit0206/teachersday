import turtle
happy=turtle.Screen()
happy.setup(1000,660)
happy.bgpic("ai.gif")
happy.register_shape("rdec.gif")
turtle=turtle.Turtle()
turtle.shape("turtle")
turtle.width(11)
  
def mov(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.lt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.pendown()

#letters
def A():
  turtle.rt(16)
  turtle.forward(60)
  turtle.rt(150)
  turtle.fd(60)
  turtle.backward(30)
  turtle.rt(90)
  turtle.fd(20)  

def D():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(9)
   for i in range(13):
      turtle.rt(13)
      turtle.fd(7)  

       
       
def Y():
   turtle.fd(40)
   turtle.left(60)
   turtle.fd(30)
   turtle.backward(30)
   turtle.rt(90)
   turtle.fd(30)
   


def H():
   turtle.fd(60)
   turtle.backward(30)
   turtle.rt(90)
   turtle.fd(30)
   turtle.lt(90)
   turtle.fd(30)
   turtle.backward(60)
   
   
def P():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(8):
       turtle.rt(20)
       turtle.fd(5)
       
    
def R():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(15):
      turtle.rt(12)
      turtle.fd(3)
   turtle.lt(120)
   turtle.fd(37)
  
def e():
  turtle.fd(60)
  turtle.backward(60)
  turtle.rt(90)
  turtle.fd(30)
  turtle.rt(180)
  turtle.fd(30)
  turtle.rt(90)
  turtle.fd(30)
  turtle.rt(90)
  turtle.fd(30)
  turtle.rt(180)
  turtle.fd(30)
  turtle.rt(90)
  turtle.fd(30)
  turtle.rt(90)
  turtle.fd(30)
  turtle.backward(30)

def t():
  turtle.fd(60)
  turtle.lt(90)
  turtle.fd(30)
  turtle.rt(180)
  turtle.fd(60)

def c():
  turtle.lt(90)
  turtle.fd(30)
  turtle.rt(90)
  turtle.fd(60)
  turtle.rt(90)
  turtle.fd(30)

def s():
  turtle.rt(90)
  turtle.fd(30)
  turtle.lt(90)
  turtle.fd(30)
  turtle.lt(90)
  turtle.fd(30)
  turtle.rt(90)
  turtle.fd(30)
  turtle.rt(90)
  turtle.fd(30)



# happy
turtle.speed(5)
turtle.width(9)
turtle.color("#ccccff")
mov(350,170)
H()
turtle.speed(8)
turtle.width(5)
mov(310,170)
A()
mov(270,170)
P()
mov(240,170)
P()
mov(190,170)
Y()

turtle.speed(5)
turtle.width(9)
mov(410,90)
t()
turtle.speed(8)
turtle.width(5)
mov(370,90)
e()
mov(325,90)
A()
mov(255,90)
c()
mov(245,90)
H()
mov(205,90)
e()
mov(165,90)
R()
mov(135,140)
turtle.fd(10)
mov(125,90)
s()

turtle.speed(5)
turtle.width(9)
mov(300,10)
D()
turtle.speed(8)
turtle.width(5)
mov(260,10)
A()
mov(205,10)
Y()

# base of cake
turtle.speed(6)
turtle.width(6)
turtle.color("white")
mov(-250,-255)
turtle.begin_fill()
turtle.lt(65)
turtle.fd(120)
turtle.rt(30)
turtle.fd(17)
turtle.rt(35)
turtle.fd(80)
for i in range(3):
    turtle.rt(30)
    turtle.fd(17)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(30)
turtle.rt(20)
turtle.fd(35)

turtle.lt(100)

turtle.fd(35)
turtle.rt(20)
turtle.fd(30)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
for i in range(3):
    turtle.fd(17)
    turtle.rt(30)
turtle.fd(80)
turtle.rt(35)
turtle.fd(17)
turtle.rt(30)  
turtle.fd(122)
turtle.lt(65)
turtle.end_fill()


# cake topping
turtle.color("#1a0d00")
mov(-250,-255)
turtle.lt(65)
turtle.fd(120)
turtle.rt(30)
turtle.fd(17)
turtle.rt(35)
turtle.fd(80)
for i in range(3):
    turtle.rt(30)
    turtle.fd(17)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(30)
turtle.rt(20)
turtle.fd(35)

turtle.lt(100)

turtle.fd(35)
turtle.rt(20)
turtle.fd(30)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
for i in range(3):
    turtle.fd(17)
    turtle.rt(30)
turtle.fd(80)
turtle.rt(35)
turtle.fd(17)
turtle.rt(30)  
turtle.fd(122)
turtle.lt(65)



turtle.color("#331a00")
mov(-253,-175)
turtle.begin_fill()
turtle.lt(65)
turtle.fd(124)
for i in range(5):
    turtle.rt(30)
    turtle.fd(17)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(30)
turtle.rt(20)
turtle.fd(35)

turtle.lt(90)

turtle.fd(35)
turtle.rt(20)
turtle.fd(30)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
for i in range(5):
    turtle.fd(17)
    turtle.rt(30)
turtle.fd(124)
turtle.end_fill()



turtle.color("#1a0d00")
turtle.width(10)
mov(-253,-175)
turtle.lt(65)
turtle.fd(124)
for i in range(5):
    turtle.rt(30)
    turtle.fd(17)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(30)
turtle.rt(20)
turtle.fd(35)

turtle.lt(90)

turtle.fd(35)
turtle.rt(20)
turtle.fd(30)
turtle.rt(15)
turtle.fd(17)
turtle.rt(15)
turtle.fd(17)
for i in range(5):
    turtle.fd(17)
    turtle.rt(30)
turtle.fd(124)


# cake layers... brown color
turtle.width(6)
mov(-250,-230)
turtle.lt(65)
turtle.fd(120)
turtle.rt(30)
turtle.fd(17)
mov(-253,-230)
turtle.rt(65)
turtle.fd(120)
turtle.lt(30)
turtle.fd(17)
mov(-250,-205)
turtle.lt(65)
turtle.fd(120)
turtle.rt(30)
turtle.fd(17)
mov(-253,-205)
turtle.rt(65)
turtle.fd(120)
turtle.lt(30)
turtle.fd(17)
turtle.width(3)
mov(-220,-170)
turtle.fd(2)
mov(-190,-190)
turtle.fd(2)
mov(-140,-165)
turtle.fd(2)
mov(-220,-210)
turtle.fd(2)
mov(-200,-200)
turtle.fd(2)
mov(-170,-215)
turtle.fd(2)
mov(-280,-170)
turtle.fd(2)
mov(-310,-190)
turtle.fd(2)
mov(-360,-165)
turtle.fd(2)
mov(-280,-210)
turtle.fd(2)
mov(-300,-200)
turtle.fd(2)
mov(-330,-215)
turtle.fd(2)

# candles
turtle.width(6)
turtle.color("yellow")
mov(-150,-95)
turtle.fd(60)
turtle.width(1)
turtle.color("black")
mov(-150,-35)
turtle.fd(5)
mov(-150,-30)
turtle.color("#ff9900")
x=12
while x>0:
    turtle.width(x)
    turtle.fd(2)
    x-=2
turtle.color("#ff0066")
turtle.width(6)
mov(-350,-95)
turtle.fd(60)
turtle.width(1)
turtle.color("black")
mov(-350,-35)
turtle.fd(5)
mov(-350,-30)
turtle.color("#ff9900")
x=12
while x>0:
    turtle.width(x)
    turtle.fd(2)
    x-=2 


# pic
turtle.shape("rdec.gif")
mov(280,-160)
happy.exitonclick()