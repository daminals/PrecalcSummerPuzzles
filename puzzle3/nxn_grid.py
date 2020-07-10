# nxn_grid.py
# This attempts to draw out all possible solutions to the problem
# Daniel Kogan, 07/09/2020

import turtle, itertools, random, math
from solvegrid import solve
from colorama import Fore, Back, Style

# TODO: Filter out impossible paths


def square(turtle, len):
    for i in range(4):
        turtle.forward(len)
        turtle.left(90)


def row(turtle, n, len):
    for i in range(n):
        square(turtle, len)
        turtle.forward(len)
    turtle.penup()
    turtle.left(180)
    turtle.forward(n * len)
    turtle.left(180)
    turtle.pendown()


def grid(turtle, m, n, len):
    for i in range(m):
        row(turtle, n, len)
        turtle.penup()
        turtle.left(90)
        turtle.forward(len)
        turtle.right(90)
        turtle.pendown()
    turtle.penup()
    turtle.right(90)
    turtle.forward(len * m)
    turtle.left(90)
    turtle.pendown()


def right_pyth(n):
    m = 2 * (n ** 2)
    return math.sqrt(m)


def diagnol(turtle, n, len):
    diagn = []
    turtle.left(45)
    m = right_pyth(n)
    for i in range(n):
        # print(i)
        position = (turtle.xcor, turtle.ycor)
        diagn.append(position)
        turtle.forward(len * (m / n))
    position = (turtle.xcor, turtle.ycor)
    diagn.append(position)
    turtle.penup()
    turtle.backward(n * len * m)
    turtle.right(45)
    turtle.pendown()
    diagn = set(diagn)
    return diagn


def main(n, size):
    wn = turtle.Screen()
    wn.setup(width=500, height=500)
    wn.tracer(0)

    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

    robit = turtle.Turtle()
    robit.penup()
    robit.goto(-248, -239)
    robit.pendown()
    grid(robit, n, n, size)
    diagn = diagnol(robit, n, size)
    # print(diagn)
    solutions = solve(n)
    # print(len(solutions))

    # print(diagn)

    solu2 = solutions.copy()
    robit.penup()
    for i in solutions:
        global destroy
        destroy = 0
        for j in i:
            position = (robit.xcor, robit.ycor)
            for x in diagn:
                if position >= x:
                    if j:
                        destroy = 1
            if j:
                robit.left(90)
                robit.forward(size)
                robit.right(90)
            else:
                robit.forward(size)
        if destroy:
            solutions.remove(i)
        destroy = 0
        robit.penup()
        robit.goto(-248, -239)
        robit.pendown()

    final_lis = []
    [final_lis.append(x) for x in solu2 if x not in solutions]
    solutions = []
    for x in final_lis:
        x = list(x)
        if not (x[2] == 1 and x[1] == 1):
            solutions.append(x)

    #print(final_lis)
    print(solutions)
    print(len(solutions))

    robit.pendown()
    robit.width(3)
    for i in solutions:
        color = random.choice(colors)
        robit.color(color)
        for j in i:
            if j:
                robit.left(90)
                robit.forward(size)
                robit.right(90)
            else:
                robit.forward(size)
        robit.penup()
        robit.goto(-248, -239)
        robit.pendown()

    while True:
        wn.update()


if __name__ == '__main__':
    main(3, 100)
