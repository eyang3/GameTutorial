WIDTH=800
HEIGHT=800

zombie = Actor('zombie_idle')
zombie.walkFrame = 0

penguin = Actor('penguin')

penguin.top = 100
penguin.left = 100
step_size = 10

def draw():
    screen.fill((128,128,128))
    zombie.draw()
    penguin.draw()

def idle():
    zombie.image = 'zombie_idle'

def zombie_action(action):
    if(action == 'walk'):
        zombie.walkFrame += 1
        frame = (zombie.walkFrame % 2) + 1
        pose_file = 'zombie_walk%s' % frame
        zombie.image = pose_file
    if(action == 'kick'):
        zombie.image = 'zombie_kick'
        if(zombie.colliderect(penguin)):
            penguin.right += 20
        clock.schedule_unique(idle, 0.1)


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

