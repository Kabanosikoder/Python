# -*- coding: utf-8 -*-
import turtle
import random
import time
import math

# Paramètres
CANNON_STEP = 10
LASER_SPEED = 4
ALIEN_SPEED = 0.4
ALIEN_SPAWN_INTERVAL = 1.2
DETECTION_RADIUS = 20

# Configuration de la fenêtre
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Space Invaders")
window.tracer(0)  # Désactiver la mise à jour automatique de l’écran

# Création du canon (partie intermédiaire)
cannon = turtle.Turtle()
cannon.penup()
cannon.color("white")
cannon.shape("circle")
cannon.setposition(0, -230)
cannon.shapesize(stretch_wid=2, stretch_len=3)

# Création de la partie supérieure du canon
def create_cannon_top():
    part2 = turtle.Turtle()
    part2.shape("triangle")
    part2.color("white")
    part2.penup()
    part2.speed(0)
    part2.setposition(0, -210)
    part2.shapesize(stretch_wid=2.5, stretch_len=1.5)
    part2.left(90)
    return part2

part2 = create_cannon_top()

# Création d’un extraterrestre
def create_alien():
    alien = turtle.Turtle()
    alien.penup()
    alien.shape("turtle")
    alien.color("green")
    alien.shapesize(stretch_wid=1.5, stretch_len=2)
    alien.setposition(random.randint(-390, 390), 250)
    alien.right(90)
    return alien

# Déplacer les extraterrestres
def move_aliens():
    global ALIEN_SPEED
    for alien in aliens[:]:
        alien.sety(alien.ycor() - ALIEN_SPEED)
        # Inverser la direction lorsque l'alien atteint les bords
        if alien.xcor() > 390 or alien.xcor() < -390:
            ALIEN_SPEED = -ALIEN_SPEED
        # Si l'alien touche le sol
        if alien.ycor() < -290:
            aliens.remove(alien)
            alien.hideturtle()
            return True
    return False

# Créer un laser
def create_laser():
    laser = turtle.Turtle()
    laser.penup()
    laser.color("red")
    laser.shape("square")
    laser.shapesize(stretch_wid=0.5, stretch_len=2)
    laser.setheading(90)
    laser.setposition(cannon.xcor(), cannon.ycor() + 20)
    return laser

# Créer une fonction pour détecter les collisions
def check_collision(laser, alien):
    distance = math.sqrt(math.pow(laser.xcor() - alien.xcor(), 2) + math.pow(laser.ycor() - alien.ycor(), 2))
    return distance < DETECTION_RADIUS

# Déplacer les lasers
def move_lasers():
    for laser in lasers[:]:
        laser.forward(LASER_SPEED)
        # Retirer les lasers qui sortent de l’écran
        if laser.ycor() > window.window_height() / 2:
            laser.clear()
            laser.hideturtle()
            lasers.remove(laser)
        # Vérifier les collisions
        for alien in aliens[:]:
            if check_collision(laser, alien):
                laser.clear()
                laser.hideturtle()
                lasers.remove(laser)
                aliens.remove(alien)
                alien.clear()
                alien.hideturtle()

# Lier les touches du clavier
def move_left():
    new_x = cannon.xcor() - CANNON_STEP
    if new_x >= - window.window_width() / 2 + 20:  # Garder le canon dans l’écran
        cannon.setx(new_x)
        part2.setx(new_x)  # Déplacer aussi la partie supérieure

def move_right():
    new_x = cannon.xcor() + CANNON_STEP
    if new_x <= window.window_width() / 2 - 20:
        cannon.setx(new_x)
        part2.setx(new_x)  # Déplacer aussi la partie supérieure

# Variables de jeu
lasers = []
aliens = []
game_running = True

# Créer un laser quand la touche espace est pressée
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(lambda: lasers.append(create_laser()), "space")

# Boucle principale du jeu
alien_timer = time.time()
while game_running:
    # Ajouter des aliens régulièrement
    if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
        aliens.append(create_alien())
        alien_timer = time.time()

    move_aliens()
    move_lasers()

    # Vérifier si un alien touche le sol
    if move_aliens():
        game_running = False

    window.update()

# Afficher "Game Over"
if not game_running:
    game_over = turtle.Turtle()
    game_over.color("red")
    game_over.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
    window.update()

# Garder la fenêtre ouverte
turtle.done()
