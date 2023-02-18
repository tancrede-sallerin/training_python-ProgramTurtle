import turtle

t = turtle.Turtle()


# t.forward(100)
# t.left(90)
# t.forward(50)
# t.backward(100)
# t.right(45)
# t.forward(200)

def escalier(taille, nb):

    for i in range(nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


#escalier(30, 10)

def carre(taille, nb):

    for i in range(nb):
        i += 1
        for a in range(nb):
            t.forward(taille*i)
            t.left(90)


carre(50, 4)


turtle.done()