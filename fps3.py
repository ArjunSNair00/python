from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Sky and ground
Sky()
ground = Entity(model='plane', scale=(100,1,100), color=color.green, collider='box')

# Player (spawned above ground!)
player = FirstPersonController()
player.y = 2  # raise player to be just above the ground

# Some cubes to shoot or walk around
for i in range(10):
    box = Entity(model='cube', color=color.orange, scale=2,
                 position=(i*4,1,5), collider='box')

# Add a gun (just for looks)
gun = Entity(model='cube', color=color.gray, scale=(0.3,0.2,1), position=(0.4,-0.4,1), parent=camera.ui)

# Simple shooting effect
def input(key):
    if key == 'left mouse down':
        mouse_ray = raycast(player.position, camera.forward, distance=100, ignore=[player,])
        if mouse_ray.hit:
            destroy(mouse_ray.entity)
            print("Hit:", mouse_ray.entity)

app.run()
