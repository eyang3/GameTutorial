import random
WIDTH=800
HEIGHT=800

zombie = Actor('zombie_idle')
zombie.walkFrame = 0

group = []
lasers = []

RED = 200, 0, 0
BOX = Rect((20, 20), (100, 20))

for i in range(0, 3):
    v = Actor('adventurer_idle')
    v.top = random.randint(100, 700)
    v.left = random.randint(100, 700)
    group.append(v)

step_size=20

def animate_laser():
    for i in lasers:
        i.right -= 10
        if(i.left < 0):
            lasers.remove(i)

def shootlasers():
    for i in group:
        if len(lasers) < 10:
            if(i.bottom > zombie.top) and (i.top < zombie.bottom):
                print('shoot laser')
                r = Rect((20, 20), (50, 20))
                r.right = i.left
                r.y = i.y
                lasers.append(r)
 

def update():
    animate_laser()

def draw():
    screen.fill((128,128,128))

    
    zombie.draw()
    for i in group:
        i.draw()
    for i in lasers:
        screen.draw.filled_rect(i, RED)
    
def idle():
    zombie.image = 'zombie_idle'
 
def victim_idle():
    for zoomie in group:
        if zoomie.image == 'adventurer_hurt':
            group.remove(zoomie)
        #zoomie.image = 'adventurer_idle' 
# does something
def zombie_action(action):
    shootlasers()
    if(action == 'walk'):
        zombie.walkFrame += 1
        frame = (zombie.walkFrame % 2) + 1
        pose_file = 'zombie_walk%s' % frame
        zombie.image = pose_file
    if(action == 'kick'):
        zombie.image = 'zombie_kick'
        for zoomie in group:
            if(zombie.colliderect(zoomie)):
                zoomie.image = 'adventurer_hurt'
                zoomie.right += 20
                if(zombie.top>zoomie.top):
                    zoomie.bottom += 20
                else:
                    zoomie.bottom -= 20
        clock.schedule_unique(idle, 0.1)
        clock.schedule_unique(victim_idle, 0.5)
    
def on_key_down(key):
    if(key == key.DOWN):
        zombie.top += step_size
        zombie_action('walk')
        if zombie.y>800:
            zombie.y=0
    if(key == key.UP):
        zombie.top -= step_size
        zombie_action('walk')
        if(zombie.y<0):
            zombie.y=800
    if(key == key.LEFT):
        zombie.right -= step_size
        zombie_action('walk')
        if(zombie.x<0):
            zombie.x=800
    if(key == key.RIGHT):
        zombie.right += step_size
        zombie_action('walk')
        if(zombie.x > 800):
            zombie.x = 0
    if(key == key.K):
        zombie_action('kick')

