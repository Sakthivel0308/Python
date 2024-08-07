import turtle
import random
import time

WIDTH, HEIGHT = 800, 800
COLORS = ['red', 'green', 'blue', 'yellow', 'black', 'purple', 'orange', 'cyan', 'pink', 'brown']

def get_no_of_racers():
    while True:
        racers = input("Enter a No of Racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number of racers must be between 2 and 10.")
        else:
            print("Invalid number of racers, try again.")

def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.left(90)
        racer.shape("turtle")
        racer.color(color)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingX, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(turtles):
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            if racer.ycor() >= HEIGHT // 2 - 20:
                return turtles.index(racer)


def init_turtle():
    screen = turtle.Screen()
    screen.title("Race Turtle Simulator")
    screen.setup(WIDTH, HEIGHT)
    return screen

racers = get_no_of_racers()
screen = init_turtle()



random.shuffle(COLORS)
colors = COLORS[:racers]

turtles = create_turtles(colors)

# Start the race
winner = race(turtles)
print(f"The winner is the turtle with color: {colors[winner]}!")

# Keep the window open
screen.mainloop()
