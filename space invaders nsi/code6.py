import turtle
import random
import time

# Paramètres du jeu
CANNON_STEP = 10
LASER_SPEED = 15
ALIEN_SPEED = 2
ALIEN_SPAWN_INTERVAL = 1.2
COLLISION_DISTANCE = 20

# Variables de jeu
lasers = []
aliens = []
game_running = True

# Configuration de la fenêtre
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Space Invaders")
window.tracer(0)

# Création du canon et des autres objets (partie basse et haute)

# Déplacer les aliens, lasers et détecter les collisions

# Boucle principale du jeu
alien_timer = time.time()
while game_running:
    if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
        create_alien()
        alien_timer = time.time()

    move_aliens()
    move_lasers()
    check_collision()

    # Vérifier si un alien touche le sol
    for alien in aliens:
        if alien.ycor() < -300:
            game_running = False
            break

    window.update()

# Afficher "Game Over"
if not game_running:
    game_over = turtle.Turtle()
    game_over.color("red")
    game_over.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
    window.update()

turtle.done()
