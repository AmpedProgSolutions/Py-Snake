import turtle
import time
import random

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("green")
win.setup(width=1280, height=720)

# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Create an empty list for snake body
segments = []

# Create the score
score = 0
score_text = turtle.Turtle()
score_text.speed(0)
score_text.color("white")
score_text.penup()
score_text.hideturtle()
score_text.goto(0, 260)
score_text.write("Score: {}".format(score),
                 align="center",
                 font=("Courier", 24, "normal"))


# Move the snake
def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)

  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)

  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)

  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)


# Change the direction
def go_up():
  if head.direction != "down":
    head.direction = "up"


def go_down():
  if head.direction != "up":
    head.direction = "down"


def go_right():
  if head.direction != "left":
    head.direction = "right"


def go_left():
  if head.direction != "right":
    head.direction = "left"


# Keyboard Bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")

# Main game loop
while True:
  win.update()

  # Check for collision with wall
  if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor(
  ) < -290:
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments on restart
    for segment in segments:
      segment.goto(1000, 1000)

    # Clear the segments list
    segments.clear()

    # Reset the score
    score = 0

    # Update the score
    score_text.clear()
    score_text.write("Score: {}".format(score),
                     align="center",
                     font=("Courier", 24, "normal"))

  # Check for collision with food
  if head.distance(food) < 20:
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x, y)

    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

    # Increase the score
    score += 10
    score_text.clear()
    score_text.write("Score: {}".format(score),
                     align="center",
                     font=("Courier", 24, "normal"))

  # Move the end segments first in reverse order
  for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
    y = segments[index - 1].ycor()
    segments[index].goto(x, y)

  # Move segment 0 to where the head is
  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

  move()

  # Check for collision with body
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0, 0)
      head.direction = "stop"

      # Hide the segments on restart
      for segment in segments:
        segment.goto(1000, 1000)

      # Clear the segments list
      segments.clear()

      # Reset the score
      score = 0

      # Update the score
      score_text.clear()
      score_text.write("Score: {}".format(score),
                       align="center",
                       font=("Courier", 24, "normal"))

  time.sleep(0.1)

# Exit the window
win.mainloop()
