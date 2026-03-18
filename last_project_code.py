

import turtle
import random

def main():
   letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
   for letter in letters:
       letter_draw(letter)
   turtle.done()
   

def letter_draw(letter):
    t = turtle.Turtle()
    t.speed(1)

    x_pos = -200 + (ord(letter) -65) * 30
    t.penup()
    t.goto(x_pos, 0)
    t.pendown()


# convert letter to number for consistency 
    value = ord(letter)
    random.seed(value)

# move to a position so drawings don't overlap
    t.penup()
    t.goto(-200 + (ord(letter) - 65) * 40, 0)
    t.pendown()
    size = 100 
    if letter == "A":
        t.left(70)
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.backward(size // 2)
        t.right(120)
        t.forward(size // 3)

    elif letter == "B":
        t.forward(size)
        t.circle(size // 2)
        t.forward(50)
        t.circle(size // 2)

    elif letter == "C":
        t.penup()
        t.forward(size // 2)
        t.pendown()
        t.circle(size // 2, 180)

    elif letter == "D":
        t.left(90)
        t.forward(size)
        t.right(90)
        t.circle(-size // 2, 180)

    else:
       for _ in range(4):
           t.forward(size)
           t.right(90)

    sides = random.randint(3, 6)

    for i in range(sides):
        length = random.randint(50, 100)
        angle = random.randint(30, 150)
        t = turtle.Turtle()

        t.forward(length)

        if random.randint(0, 1) == 0:
            t.left(angle)
    else:
            t.right(angle)

# add a small feature 
    if random.randint(0, 1) == 1:
       t.penup()
       t.forward(15)
       t.pendown()
       t.circle(random.randint(5, 15))


if __name__ == "__main__":
    main()

















if __name__ = = "__main__":
    
