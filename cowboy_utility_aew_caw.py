#player1() function
def player1(ori):
    #cowboy face
    ori.setheading(0)
    ori.penup()
    ori.goto(-300,0)
    ori.pendown()
    ori.circle(30)
    ori.right(90)
    ori.forward(100)
    #cowboy pants
    ori.right(25)
    ori.pencolor("blue")
    ori.forward(50)
    ori.penup()
    ori.goto(-300,-100)
    ori.pendown()
    ori.left(50)
    ori.forward(50)
    #cowboy hat
    ori.penup()
    ori.pencolor("black")
    ori.goto(-300,-50)
    ori.pendown()
    ori.left(65)
    ori.forward(35)
    ori.penup()
    ori.goto(-350,50)
    ori.pendown()
    ori.fillcolor("brown")
    ori.begin_fill()
    ori.forward(100)
    ori.left(135)
    ori.forward(10)
    ori.left(45)
    ori.forward(88)
    ori.left(45)
    ori.forward(10)
    ori.end_fill()
    ori.penup()
    ori.goto(-330,58)
    ori.pendown()
    ori.fillcolor("brown")
    ori.begin_fill()
    ori.right(145)
    ori.forward(20)
    ori.right(80)
    ori.forward(50)
    ori.right(80)
    ori.forward(20)
    ori.end_fill()
    #cowboy eyebrow
    ori.penup()
    ori.goto(-293,40)
    ori.pendown()
    ori.left(55)
    ori.forward(10)
    #cowboy eye
    ori.penup()
    ori.goto(-293,25)
    ori.pendown()
    ori.pencolor("blue")
    ori.fillcolor("blue")
    ori.begin_fill()
    ori.circle(3)
    ori.end_fill()
    #cowboy gun
    ori.penup()
    ori.pencolor("gray")
    ori.fillcolor("gray")
    ori.begin_fill()
    ori.left(25)
    ori.goto(-270,-35)
    ori.pendown()
    ori.forward(30)
    ori.right(90)
    ori.forward(5)
    ori.right(90)
    ori.forward(25)
    ori.left(90)
    ori.forward(15)
    ori.right(90)
    ori.forward(5)
    ori.right(90)
    ori.forward(20)
    ori.end_fill()
    return


#player2() function
def player2(ori):
    #cowboy face
    ori.pencolor("black")
    ori.setheading(0)
    ori.penup()
    ori.goto(300,0)
    ori.pendown()
    ori.circle(30)
    ori.right(90)
    ori.forward(100)
    ori.right(25)
    #cowboy pants
    ori.pencolor("red")
    ori.forward(50)
    ori.penup()
    ori.goto(300,-100)
    ori.pendown()
    ori.left(50)
    ori.forward(50)
    #cowboy hat
    ori.penup()
    ori.pencolor("black")
    ori.goto(300,-50)
    ori.pendown()
    ori.right(115)
    ori.forward(35)
    ori.left(180)
    ori.penup()
    ori.goto(250,50)
    ori.pendown()
    ori.fillcolor("black")
    ori.begin_fill()
    ori.forward(100)
    ori.left(135)
    ori.forward(10)
    ori.left(45)
    ori.forward(88)
    ori.left(45)
    ori.forward(10)
    ori.end_fill()
    ori.penup()
    ori.goto(270,58)
    ori.pendown()
    ori.fillcolor("black")
    ori.begin_fill()
    ori.right(145)
    ori.forward(20)
    ori.right(80)
    ori.forward(50)
    ori.right(80)
    ori.forward(20)
    ori.end_fill()
    #cowboy eyebrow
    ori.penup()
    ori.goto(293,40)
    ori.pendown()
    ori.right(60)
    ori.forward(10)
    #cowboy eye
    ori.penup()
    ori.goto(293,30)
    ori.pendown()
    ori.pencolor("red")
    ori.fillcolor("red")
    ori.begin_fill()
    ori.circle(3)
    ori.end_fill()
    #cowboy gun
    ori.penup()
    ori.pencolor("gray")
    ori.fillcolor("gray")
    ori.begin_fill()
    ori.right(40)
    ori.goto(270,-35)
    ori.pendown()
    ori.forward(30)
    ori.left(90)
    ori.forward(5)
    ori.left(90)
    ori.forward(25)
    ori.right(90)
    ori.forward(15)
    ori.left(90)
    ori.forward(5)
    ori.left(90)
    ori.forward(20)
    ori.end_fill()
    return

#gunshot explosion function
def explosion(ori, is_player1, random):
    if is_player1:
        ori.penup()
        ori.goto(-240,-35)
        ori.pendown()
        ori.pencolor("red")
        ori.fillcolor("yellow")
        ori.begin_fill()
        side_length = random.randint(5,30)
        for i in range(6):
            ori.forward(side_length)
            ori.left(255)
            ori.forward(side_length)
            ori.left(45)
        ori.end_fill()
    else:
        ori.goto(240,-35)
        ori.pendown()
        ori.pencolor("red")
        ori.fillcolor("yellow")
        ori.begin_fill()
        side_length = random.randint(5,30)
        for i in range(6):
            ori.forward(side_length)
            ori.right(255)
            ori.forward(side_length)
            ori.right(45)
        ori.end_fill()
    return

#blood spurt function
def blood_spurt():
    return