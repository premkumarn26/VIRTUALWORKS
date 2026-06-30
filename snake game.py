Snake Game:

import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body
segments = []

# Score
score = 0

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)
    elif head.direction == "down":
        head.sety(y - 20)
    elif head.direction == "left":
        head.setx(x - 20)
    elif head.direction == "right":
        head.setx(x + 20)

# Keyboard controls
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main Game Loop
while True:
    screen.update()
    time.sleep(0.1)

    move()

    # Collision with wall
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):
        print("Game Over!")
        break

    # Collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        print("Score:", score)

    # Move body
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Check collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            print("Game Over!")
            screen.bye()
            exit()

turtle.done()
