# Ajouter du son avec pygame
import pygame
pygame.mixer.init()

# Charger les sons
tir_sound = pygame.mixer.Sound('tir.wav')
collision_sound = pygame.mixer.Sound('collision.wav')
game_over_sound = pygame.mixer.Sound('gameover.wav')

# Jouer le son du tir
def shoot_laser():
    laser = turtle.Turtle()
    laser.penup()
    laser.color("red")
    laser.shape("square")
    laser.shapesize(stretch_wid=0.5, stretch_len=2)
    laser.setheading(90)
    laser.setposition(cannon.xcor(), cannon.ycor() + 20)
    lasers.append(laser)
    tir_sound.play()  # Jouer le son du tir
