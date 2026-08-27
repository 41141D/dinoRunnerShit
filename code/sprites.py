from setting import *
import raylib as rl
from pyray import *
class Sprites:
    def __init__(self, texture, pos):
        self.texture = texture
        self.pos = pos

    def get_colission_circle(self):
        center_x = self.pos.x + (self.texture.width * 4.99) / 2
        center_y = self.pos.y + (self.texture.height * 4.99) / 2
        radius = (self.texture.width * 4.99) / 2

        return (center_x, center_y, radius)

    def draw(self):
        draw_texture_ex(self.texture, self.pos, 0, 4.99, WHITE)


class MovingSprites(Sprites):
    def __init__(self, frames, pos, speed):
        self.frames = frames if isinstance(frames, list) else [frames]
        super().__init__(self.frames[0], pos)

        self.speed = speed
        self.frame_index = 0

    def update(self, dt):
        self.pos.x -= self.speed * dt

        if len(self.frames) > 1:
            self.frame_index += dt * 15
            self.frame_index %= len(self.frames)
            self.texture = self.frames[int(self.frame_index)]




class Dino(Sprites):
    def __init__(self, textures, jump,pos, jump_sound):
        self.textures = textures
        self.jump = jump
        super().__init__(textures[0], pos)
        self.velocity = 0
        self.jump_sound = jump_sound
        self.ground_y = 436
        self.is_grounded = False
        self.frame_index =0

    def update(self,dt):
        self.velocity += 0.8
        self.pos.y += self.velocity
        if self.pos.y >= self.ground_y:
            self.pos.y = self.ground_y
            self.velocity = 0
            self.is_grounded = True
        else:
            self.is_grounded = False

        if is_key_pressed(rl.KEY_W) and self.is_grounded:
            self.velocity = -19
            play_sound(self.jump_sound)
            self.is_grounded = False
        self.frame_index += dt*15
        self.frame_index %= 2
    def draw(self):

        self.texture = self.textures[int(self.frame_index)] if self.pos.y > 430 else self.jump
        super().draw()
class Score:
    def __init__(self, font):
        self.font = font
    def draw(self):
        draw_text_ex(self.font,f"SCORE : {get_time():.0f}",Vector2(520,50),40,2,DARKGRAY)