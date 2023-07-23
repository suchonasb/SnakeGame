#Project: Snake Game using Turtle and Python

import turtle
import time
import random

# color palette
# #BF0A30 Strong Red
# #4CBB17 Strong Green

# Score Variables

delay = 0.1
score = 0
high_score = 0

# Creating the game window

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)


# Head of the snake

head = turtle.Turtle()
head.shape("square")
head.color("#BF0A30")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food for the snake

food = turtle.Turtle()
colors = random.choice(['orange', 'black', 'purple'])
shapes = random.choice(['circle', 'triangle', 'square'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# Creating the snake

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0 Highest Score: 0", align="center", font=("helvetica", 18, "bold"))


# assigning key directions

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
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

segments = []

# Creating a new turtle for displaying "Game Over" message

game_over_turtle = turtle.Turtle()
game_over_turtle.speed(0)
game_over_turtle.color("red")
game_over_turtle.penup()
game_over_turtle.hideturtle()
game_over_turtle.goto(0, 0)


# Function to show "Game Over" message
def show_game_over():
    game_over_turtle.penup()
    game_over_turtle.color("#BF0A30")
    game_over_turtle.hideturtle()
    game_over_turtle.goto(0, 0)
    game_over_turtle.write("GAME OVER", align="center", font=("Helvetica", 30, "bold"))


# Function to reset the game
def reset_game():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    delay = 0.1
    pen.clear()
    pen.write("Score : {} Highest Score : {} ".format(score, high_score), align="center", font=("Helvetica", 24, "bold"))


# Main Game Loop

while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 230 or head.ycor() < -290:
        wn.tracer(1)  # Allow the "Game Over" message to be displayed immediately
        show_game_over()
        reset_game()
        game_over_turtle.clear()
        wn.tracer(0)  # Set the tracer back to 0 for smooth gameplay
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        colors = random.choice(['orange', 'black', 'purple'])
        shapes = random.choice(['circle', 'triangle', 'square'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} Highest Score : {} ".format(
            score, high_score), align="center", font=("helvetica", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 220)
        food.goto(x, y)

        # Adding segment

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#4CBB17")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} Highest Score : {} ".format(
            score, high_score), align="center", font=("helvetica", 24, "bold"))

    # Checking for head collisions with body segments

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['orange', 'black', 'purple'])
            shapes = random.choice(['circle', 'triangle', 'square'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} Highest Score : {} ".format(
                score, high_score), align="center", font=("helvetica", 24, "bold"))

    time.sleep(delay)

wn.mainloop()
