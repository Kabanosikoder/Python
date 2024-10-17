# -*- coding: utf-8 -*-
import turtle
import random
import time

# Paramètres
LASER_SPEED = 15
ALIEN_SPEED = 2
ALIEN_SPAWN_INTERVAL = 1.2
DETECTION_RADIUS = 20

# Listes pour stocker les lasers et les extraterrestres
lasers = []
aliens = []

# Créer une fonction pour détecter les collisions
def check_collision(laser, alien):
    distance = laser.distance(alien)
    if distance < DETECTION_RADIUS:
        laser.hideturtle()
        alien.hideturtle()
        lasers.remove(laser)
        aliens.remove(alien)
        return True
    return False

# Boucle de détection des collisions dans la boucle principale
while True:
    # Déplacer les extraterrestres et les lasers
    for laser in lasers.copy():
        laser.forward(LASER_SPEED)
    for alien in aliens.copy():
        if check_collision(laser, alien):
            break  # Sortir de la boucle si une collision est détectée

    # Autres parties du jeu ...
    window.update()
