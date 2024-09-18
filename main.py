#Levell Kensey
#Date: 8/1/2024
#CS 111 Final Project, but continued as a personal project 

import turtle
import random

color_player = 0
shape_player = 0
shape_cpu = int(random.randint(1, 5))
color_cpu = int(random.randint(0, 7))
color_ball = 0
shape_ball = 0
custom_background = 0

player = turtle.Turtle()  #player turtle
ball = turtle.Turtle()  #ball turtle
cpu = turtle.Turtle()  #cpu turtle
player.hideturtle()
ball.hideturtle()
cpu.hideturtle()

cpu.shapesize(4, 0.5, 1)
cpu.penup()
ball.penup()
cpu.setheading(180)
player.shapesize(4, 0.5, 1)
player.penup()
player.goto(-200, 0)
cpu.goto(200, 0)

# Fullscreen the canvas
screen = turtle.Screen()
screen.bgcolor('white')
screen.setup(width=700, height=500)


def stall(times):
  stalling = turtle.Turtle()
  stalling.hideturtle()
  stalling.penup()
  stalling.speed(1)
  if times >= 1:
    for i in range(times):
      stalling.goto(-100, 0)
      stalling.goto(100, 0)
  else:
    stalling.speed(times)
    stalling.goto(-100, 0)
    stalling.goto(100, 0)


# start the first sequence on the screen
beginning_text = turtle.Turtle()
beginning_text.hideturtle()
beginning_text.penup()
beginning_text.goto(0, 150)
beginning_text.color('black')
style = ('Courier', 30, 'normal')
stylethree = ('Courier', 15, 'normal')
beginning_text.write('(Maximize Screen for best efficiency)',
                     font=stylethree,
                     align='center')
stall(4)
beginning_text.clear()
beginning_text.write('Welcome to PONG, an old arcade game similar to tennis!',
                     font=stylethree,
                     align='center')
stall(4)
beginning_text.clear()
beginning_text.write(
    'The rules are simple!\nJust make sure to reflect the ball when it comes to your paddle!\n (Try to hit it in the middle of your paddle)\n The first person to 5 wins, and there\'s three levels to beat!',
    font=stylethree,
    align='center')
stall(8)
beginning_text.clear()
beginning_text.goto(0, 100)
beginning_text.write(
    "Now, let's get into the customization!\n  You'll be able to customize your paddle and the ball,\n while your opponent (a cpu) will choose a random paddle for itself.",
    font=stylethree,
    align='center')
stall(7)
beginning_text.clear()
beginning_text.goto(0, 160)
beginning_text.write('CUSTOMIZATION', font=style, align='center')

#lists for custom shapes and colors and backgrounds
custom_list_shape = [
    "square", "classic", "circle", "triangle", "turtle", "arrow"
]
custom_list_color = [
    'white', 'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink'
]
custom_list_background = [
    'bgimage1.gif', 'bgimage2.gif', 'bgimage3.gif', 'bgimage4.gif',
    'bgimage5.gif', 'bgimage6.gif'
]

ttwo = turtle.Turtle()
ttwo.hideturtle()
ttwo.penup()
ttwo.goto(0, -150)
ttwo.color('black')
styletwo = tuple(['Courier', 10, 'normal'])

tthree = turtle.Turtle()
tthree.hideturtle()
tthree.penup()
tthree.goto(0, 50)
tthree.shapesize(10, 4, 2)
#tthree.write('Press "Esc" to go back to the main menu.' ,font=styletwo,align='center')


def player_color_next():
  ttwo.clear()
  global color_player
  color_player += 1
  #write the color on the screen
  ttwo.write(custom_list_color[color_player % 8],
             font=stylethree,
             align='center')
  tthree.color(custom_list_color[color_player % 8])
  player.color(custom_list_color[color_player % 8])


def player_shape_next():
  ttwo.clear()
  global shape_player
  shape_player += 1
  #write the shape on the screen
  ttwo.write(custom_list_shape[shape_player % 6],
             font=stylethree,
             align='center')
  tthree.shape(custom_list_shape[shape_player % 6])
  player.shape(custom_list_shape[shape_player % 6])


def ball_color_next():
  ttwo.clear()
  global color_ball
  color_ball += 1
  #write the color on the screen
  ttwo.write(custom_list_color[color_ball % 8],
             font=stylethree,
             align='center')
  tthree.color(custom_list_color[color_ball % 8])
  ball.color(custom_list_color[color_ball % 8])


def ball_shape_next():
  ttwo.clear()
  global shape_ball
  shape_ball += 1
  #write the shape on the screen
  ttwo.write(custom_list_shape[shape_ball % 6],
             font=stylethree,
             align='center')
  tthree.shape(custom_list_shape[shape_ball % 6])
  ball.shape(custom_list_shape[shape_ball % 6])


def background_next():
  ttwo.clear()
  global custom_background
  custom_background += 1
  #write the shape on the screen
  ttwo.color('white')
  ttwo.write(custom_list_background[custom_background % 6],
             font=stylethree,
             align='center')
  screen.bgpic(custom_list_background[custom_background % 6])


def revert_background():
  screen.bgpic("")
  screen.bgcolor('white')
  ttwo.color('black')


#function that changes spacebar and backspace to only print nothing, to avoid potential errors when the game starts
def do_nothing():
  print('Nothing.')


def customize_screen1():
  ttwo.clear()
  ttwo.color('black')
  ttwo.write(
      'Press the right key to choose the next color for your paddle.\n When you choose the one you like, press the spacebar to move on!',
      font=styletwo,
      align='center')
  tthree.showturtle()
  screen.onkeypress(player_color_next, "Right")
  screen.onkeypress(customize_screen2, "space")


def customize_screen2():
  ttwo.clear()
  ttwo.color('black')
  ttwo.write(
      'Press the D key to choose the next shape for your paddle.\n When you choose the one you like, press the spacebar to move on! Press backspace to go to the previous page.',
      font=styletwo,
      align='center')
  tthree.showturtle()
  screen.onkeypress(do_nothing, "Right")
  screen.onkeypress(player_shape_next, "d")
  screen.onkeypress(customize_screen3, "space")
  screen.onkeypress(customize_screen1, "BackSpace")


def customize_screen3():
  ttwo.clear()
  ttwo.color('black')
  ttwo.write(
      'Press the right key to choose the next color for the ball.\n Make sure you can see it! When you choose the one you like, press the spacebar to move on!\n Press backspace to go to the previous page.',
      font=styletwo,
      align='center')
  tthree.shape('circle')
  tthree.color('red')
  tthree.showturtle()
  screen.onkeypress(do_nothing, "d")
  screen.onkeypress(ball_color_next, "Right")
  screen.onkeypress(customize_screen4, "space")
  screen.onkeypress(customize_screen2, "BackSpace")


def customize_screen4():
  ttwo.clear()
  ttwo.color('black')
  ttwo.write(
      'Press the D key to choose the next shape for the ball.\n When you choose the one you like, press the spacebar to move on! Press backspace to go to the previous page.',
      font=styletwo,
      align='center')
  tthree.showturtle()
  screen.onkeypress(do_nothing, "Right")
  screen.onkeypress(ball_shape_next, "d")
  screen.onkeypress(customize_screen5, "space")
  screen.onkeypress(customize_screen3, "BackSpace")


def customize_screen5():
  ttwo.clear()
  ttwo.color('black')
  ttwo.write(
      'Press the Right key to choose a background image (optional).\n When you choose the one you like, press the spacebar to move on!\n To go back to the default background, press W.\n Press backspace to go to the previous page.\n (It\'s best to revert the background to white first if you are going to the previous page)',
      font=styletwo,
      align='center')
  screen.onkeypress(do_nothing, 'd')
  screen.onkeypress(background_next, "Right")
  screen.onkeypress(customize_screen_last, "space")
  screen.onkeypress(customize_screen4, 'BackSpace')
  screen.onkeypress(revert_background, "w")


def customize_screen_last():
  ttwo.clear()
  tthree.hideturtle()
  screen.onkeypress(do_nothing, 'Right')
  screen.onkeypress(do_nothing, 'w')
  cpu.shape(custom_list_shape[shape_cpu % 6])
  cpu.color(custom_list_color[color_cpu % 8])
  ttwo.goto(ttwo.xcor() + 10, ttwo.ycor())
  ttwo.color('white')
  ttwo.write(
      'Press the spacebar to start the game!\n Press backspace to go to the previous page.\n Remember, once you start, you can\'t go back to change your selection!',
      font=styletwo,
      align='center')
  screen.onkeypress(game_start, "space")
  screen.onkeypress(customize_screen5, "BackSpace")
  #screen.onkeypress(game_start, "Spacebar")


#calling the function for the first customization screen, which is the first screen the user sees
customize_screen1()


#starts the function for the game
def game_start():
  beginning_text.clear()
  ttwo.clear()
  screen.onkeypress(do_nothing, "BackSpace")
  screen.onkeypress(do_nothing, "space")

  #controls for player
  def move_up():
    player.sety(player.ycor() + 10)
    if player.ycor() >= 250:
      player.sety(250)

  def move_down():
    player.sety(player.ycor() - 10)
    if player.ycor() <= -250:
      player.sety(-250)

  # functions which move the ball to various directions
  def ball_up():
    ball.sety(ball.ycor() + 10)

  def ball_down():
    ball.sety(ball.ycor() - 10)

  def ball_left():
    ball.setx(ball.xcor() - 10)

  def ball_right():
    ball.setx(ball.xcor() + 10)

  #continuously moves the ball either right or left
  def ball_directionx(directionx):
    if directionx:
      ball_right()
    else:
      ball_left()

  #continuously moves the ball either up or down
  def ball_directiony(directiony):
    if directiony:
      ball_up()
    else:
      ball_down()

  #controls for cpu
  def cpu_moveup(amt):
    cpu.sety(cpu.ycor() + amt)
    if cpu.ycor() == 250:
      cpu_movedown(amt)

  def cpu_movedown(amt):
    cpu.sety(cpu.ycor() - amt)
    if cpu.ycor() == -250:
      cpu_moveup(amt)


#cpu movement, 2+ parameters

  def cpu_moving_targeted(amt, speed, amt2):
    cpu.speed(speed)
    if (cpu.ycor() > ball.ycor()):
      cpu_movedown(amt)
    else:
      cpu_moveup(amt2)

  #writes the scores of both the player and CPU
  def write_scores():
    playerscore_text.clear()
    cpuscore_text.clear()
    playerscore_text.write("Player's Score: " + str(playerscore),
                           False,
                           align='left',
                           font=('Arial', 14, 'normal'))
    cpuscore_text.write("CPU's Score: " + str(cpuscore),
                        False,
                        align='right',
                        font=('Arial', 14, 'normal'))
    if playerscore == 5:
      stall(1)
      playerscore_text.clear()
      cpuscore_text.clear()
      playerscore_text.goto(0, 100)
      playerscore_text.write("Player Wins!",
                             False,
                             align='center',
                             font=('Arial', 20, 'normal'))
      stall(2)
      playerscore_text.clear()
    elif cpuscore == 5:
      stall(1)
      playerscore_text.clear()
      cpuscore_text.clear()
      cpuscore_text.goto(0, 100)
      cpuscore_text.write("CPU Wins!",
                          False,
                          align='center',
                          font=('Arial', 20, 'normal'))
      stall(2)
      cpuscore_text.clear()
    playerscore_text.goto(-200, 200)
    cpuscore_text.goto(200, 200)

  #function to write the level
  def write_level(level):
    level_text.clear()
    if level <= 3:
      level_text.write("Level: " + str(level),
                       False,
                       align='center',
                       font=('Arial', 25, 'normal'))
    else:
      level_text.write("You won! Thank you for playing!",
                       False,
                       align='center',
                       font=('Arial', 25, 'normal'))

  # Change screen size/color
  screen.setup(width=500, height=500)
  screen.bgcolor("black")
  #calls functions for player controls
  screen.onkeypress(move_up, "Up")
  screen.onkeypress(move_down, "Down")

  #amount of times the cpu will move
  player.goto(-240, 0)
  cpu.goto(240, 0)

  direction = int(random.randint(1, 2))
  direction = int(random.randint(1, 4))
  if direction == 1:  #randomly selects the direction of the ball each time a point is awarded
    directionx = True
    directiony = False
  elif direction == 2:
    directionx = False
    directiony = True
  elif direction == 3:
    directionx = True
    directiony = True
  else:
    directionx = False
    directiony = False
  #creates text turtles, their colors, and positions them
  playerscore_text = turtle.Turtle()
  level_text = turtle.Turtle()
  cpuscore_text = turtle.Turtle()
  playerscore_text.hideturtle()
  cpuscore_text.hideturtle()
  level_text.hideturtle()
  playerscore_text.color('blue')
  cpuscore_text.color('red')
  level_text.color('white')
  level_text.penup()
  playerscore_text.penup()
  cpuscore_text.penup()
  playerscore_text.goto(-200, 200)
  cpuscore_text.goto(200, 200)
  level_text.goto(0, 100)

  ball.showturtle()
  player.showturtle()
  cpu.showturtle()
  level = 1
  playerscore = 0
  cpuscore = 0
  write_level(level)
  stall(5)
  level_text.clear()
  write_scores()
  while True:  #first who gets to 5 wins
    ball_directionx(directionx)
    ball_directiony(directiony)
    if ball.xcor() >= 250:  #if ball hits right wall, award point to player
      playerscore += 1
      ball.goto(0, 0)
      cpu.goto(240, 0)
      stall(1)
      direction = int(random.randint(1, 4))
      if direction == 1:  #randomly selects the direction of the ball each time a point is awarded
        directionx = True
        directiony = False
      elif direction == 2:
        directionx = False
        directiony = True
      elif direction == 3:
        directionx = True
        directiony = True
      else:
        directionx = False
        directiony = False
      write_scores()
    elif cpu.xcor() == ball.xcor() and (cpu.ycor() - ball.ycor() <= 30
                                        and cpu.ycor() - ball.ycor()
                                        >= -30):  #if cpu hits ball, reflect it
      ball.setheading(180)
      directionx = False
    elif ball.xcor() <= -242:  #if ball hits left wall, award point to cpu
      cpuscore += 1
      ball.goto(0, 0)
      cpu.goto(240, 0)
      stall(1)
      direction = int(random.randint(1, 4))
      if direction == 1:  #randomly selects the direction of the ball each time a point is awarded
        directionx = True
        directiony = False
      elif direction == 2:
        directionx = False
        directiony = True
      elif direction == 3:
        directionx = True
        directiony = True
      else:
        directionx = False
        directiony = False
      write_scores()
    elif (player.xcor() == ball.xcor() and
          (player.ycor() - ball.ycor() <= 30 and player.ycor() - ball.ycor()
           >= -30)):  #if user hits ball, reflect it
      ball.setheading(0)
      directionx = True
    if ball.ycor() >= 250:
      directiony = False
    elif ball.ycor() <= -250:
      directiony = True
    if level == 1:
      cpu_moving_targeted(5, 1, 5)
      stall(0.5)
    elif level == 2:
      cpu_moving_targeted(8.5, 1, 8.5)
      stall(0.5)
    elif level == 3:
      cpu_moving_targeted(10, 1, 10)
      stall(0.45)
    if playerscore == 5:
      level += 1
      write_scores()
      if level <= 3:
        write_level(level)
        stall(3)
        level_text.clear()
      playerscore = 0
      cpuscore = 0
      write_scores()
    elif cpuscore == 5:
      write_scores()
      screen.bye()
    if level == 4:
      screen.bye()

screen.listen()
screen.mainloop()