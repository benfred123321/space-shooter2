import pgzrun
import random

HEIGHT = 800
WIDTH = 1200
white = (255,255,255)
blue =  (10,10,255)

ship = Actor("galaga")
ship.pos = (WIDTH//2,HEIGHT-60)
 
alien = Actor("bug")
 
speed=5
bullets = []
enemies = []
score = 0
derection = 1
ship.dead = False
ship.countdown = 90

for x in range(8):
    for y in range(4):
        alien = Actor("bug")
        enemies.append(alien)
        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y 

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullets.append(bullet)
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 50 

def update():
    pass




def draw():
    screen.clear()
    screen.fill(blue)
    if ship.dead == False:
        ship.draw()
    for alien in enemies:
        alien.draw()
    for bullet in bullets:
        bullet.draw()











pgzrun.go()