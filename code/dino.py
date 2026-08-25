import random
from _pyrepl.commands import clear_screen
from setting import *
import raylib
from pyray import *
from cstm_timer import Timer
from sprites import Dino,MovingSprites
class Game:
    def __init__(self):
        init_window(1280,720,"dinoRunner")
        init_audio_device()
        set_target_fps(75)
        self.sprite_list = []
        self.import_asses()
        self.timers ={"obstacle":Timer(3,self.spawn_obstacle,True,True),
                      "cloud":Timer(1,self.spawn_cloud,True,True)}
        self.dino_rotation = 0
        self.dino_pos = Vector2(POS_X,POS_Y)
        self.dino_text = load_texture(
            r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\dino\eggno.png")
        self.dino_jump_sound = load_sound(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\audio\jump.wav")
        self.dino = Dino(self.assets["player_assets"],self.assets["player_jump"],self.dino_pos,self.dino_jump_sound)


    def import_asses(self):
        self.assets = {
            'player_assets' : [load_texture(rf"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\dino\run{i}.png") for i in range(2)],
            "player_jump" : load_texture(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\dino\jump.png"),
            "cacti": [load_texture(rf"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\cactii\cactus{i}.png") for i in range(4)]
        }
    def spawn_cloud(self):
        print("spawning cloud")
    def spawn_obstacle(self):
        sprite = MovingSprites(random.choice(self.assets["cacti"]),Vector2(1200,480),7.6)
        self.sprite_list.append(sprite)
    def update(self,dt):
        self.dino.update(dt)
        for timer in self.timers.values():
            timer.update()
        for sprite in self.sprite_list:
            sprite.update(2)
    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)
        draw_line_ex(Vector2(0, line_pos), Vector2(1280, line_pos), 10.5, GRAY)
        self.dino.draw()
        for sprite in self.sprite_list:
            sprite.draw()
        end_drawing()



    def run(self):
        while not window_should_close():
            self.draw()
            dt = get_frame_time()
            self.update(dt)
        close_window()



if __name__ == "__main__":
    game = Game()
    game.run()
