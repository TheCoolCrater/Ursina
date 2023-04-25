from ursina import *

app = Ursina()
player = Entity(model="mdels/racer.fbx", texture="mdels/Ch20_1001_Diffuse.png", scale_y = 0.005, scale_x = 0.005, scale_z = 0.005)


def update():
    player.x += held_keys["d"] * 0.01
    player.x -= held_keys["a"] * 0.01
    player.y += held_keys["w"] * 0.01
    player.y -= held_keys["s"] * 0.01
    player.rotation_x += held_keys["q"] * 5
    player.rotation_y += held_keys["e"] * 30


app.run()