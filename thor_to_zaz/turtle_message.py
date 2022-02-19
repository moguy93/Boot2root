import turtle

with open('turtle', 'r') as f:
    lines = f.readlines()

turtle.color('black', 'white')

turtle.begin_fill()

def move(tokens, on):
    steps = int(tokens[1])
    if tokens[0] == "Avance":
        turtle.forward(steps)
    elif tokens[0] == "Recule":
        turtle.backward(steps)


def rotate(tokens):
    if tokens[1] == "gauche":
        turtle.left(int(tokens[3]))
    elif tokens[1] == "droite":
        turtle.right(int(tokens[3]))

on = True

for line in lines:

    tokens = line.split(' ')
    nb_tokens = len(tokens)

    print(tokens)
    print(nb_tokens)
    if nb_tokens != 5 and nb_tokens != 3:
        on = True if on == False else False
        continue

    if nb_tokens == 3:
        move(tokens, on)
    else:
        rotate(tokens)


turtle.end_fill()
turtle.done()
