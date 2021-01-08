import pygame
import random
WIDTH=800
HEIGHT=800
background = pygame.image.load("images/background.png")

zombie = Actor('zombie_idle')
zombie.walkFrame = 0

victims = []
for m in range(0,3):
  v = Actor('adventurer_idle')
  v.top = random.randint(200, 600)
  v.left = random.randint(200, 600)
  victims.append(v)

step_size = 10

def draw():
    screen.clear()
    screen.blit("background",(0,0))
    #screen.fill((128,128,128))
    zombie.draw()
    for v in victims:
      v.draw()

def idle():
    zombie.image = 'zombie_idle'

def victim_idle():
    for v in victims:
      if(v.image == 'adventurer_hurt'):
        v.image = 'adventurer_idle'
        victims.remove(v)
# does something
def zombie_action(action):
    if(action == 'walk'):
        zombie.walkFrame += 1
        frame = (zombie.walkFrame % 2) + 1
        pose_file = 'zombie_walk%s' % frame
        zombie.image = pose_file
    if(action == 'kick'):
        zombie.image = 'zombie_kick'
        for v in victims:
          if(zombie.colliderect(v)):
            v.image = 'adventurer_hurt'
            v.image = 'adventurer_hurt'
            v.right += 20
            if(zombie.top>v.top):
                v.bottom += 20
            else:
                v.bottom -= 20
        clock.schedule_unique(idle, 0.1)
        clock.schedule_unique(victim_idle, 0.5)

def on_key_down(key):
    if(key == key.DOWN):
        zombie.top += step_size
        zombie_action('walk')
    if(key == key.UP):
        zombie.top -= step_size
        zombie_action('walk')
    if(key == key.LEFT):
        zombie.right -= step_size
        zombie_action('walk')
    if(key == key.RIGHT):
        zombie.right += step_size
        zombie_action('walk')
    if(key == key.K):
        zombie_action('kick')