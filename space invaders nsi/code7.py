# Ajouter un chronomètre et un score
import turtle
import random
import time

# Paramètres du jeu
CANNON_STEP = 10
LASER_SPEED = 15
ALIEN_SPEED = 2
ALIEN_SPAWN_INTERVAL = 1.2
COLLISION_DISTANCE = 20
SCORE = 0

# Variables de jeu
lasers = []
aliens = []
game_running = True
start_time = time.time()

# Création de la fenêtre
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Space Invaders")
window.tracer(0)

# Création du canon et des autres éléments comme dans les étapes précédentes ...

# Affichage du temps et du score
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.setposition(350, 250)
score_display.color("white")

# Mettre à jour le score et le temps
def update_display():
    elapsed_time = time.time() - start_time
    score_display.clear()
    score_display.write(f"Temps : {elapsed_time:.1f}s\nScore : {SCORE}",
                        align="right", font=("Arial", 14, "normal"))

# Boucle principale du jeu
alien_timer = time.time()
while game_running:
    if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
        create_alien()
        alien_timer = time.time()

    update_display()
    window.update()

# Afficher "Game Over" quand le jeu se termine ...
turtle.done()
