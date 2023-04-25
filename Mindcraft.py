from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

random.seed(0)
Entity.default_shader = lit_with_shadows_shader


ground = Entity(model='plane', collider='box', scale=1000, texture='grass', texture_scale=(4,4))

player = FirstPersonController(model='', z=-10, color=color.orange, origin_y=-.5, speed=8, scale=0.005)
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))


for i in range(16):
    Entity(model='', origin_y=0.001, scale=7, scale_y=10, texture='', texture_scale=(1,2),
        z=random.uniform(-20, 20) + 2,
        x=random.uniform(-20, 20) + 2,
        collider='box',
        # scale_y = random.uniform(2,3),
        color=color.hsv(0, 0, random.uniform(.9, 1))
        )


class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(model='ummy_obj.obj', scale_y=2, origin_y=-.5, color=color.light_gray, collider='box', **kwargs)
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self):
        dist = distance_xz(player.position, self.position)
        if dist > 40:
            return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)


        self.look_at_2d(player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == player:
            if dist > 2:
                self.position += self.forward * time.dt * 5



app.run()