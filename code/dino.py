import random
from setting import *
import raylib
from pyray import *
from cstm_timer import Timer
from sprites import Dino, MovingSprites, Score


class Game:
    def __init__(self):
        init_window(1280, 720, "dinoRunner")
        init_audio_device()
        set_target_fps(75)

        self.sprite_list = []
        self.colission_check_list = []

        self.import_asses()

        self.timers = {
            "obstacle": Timer(3, self.spawn_obstacle, True, True),
            "cloud": Timer(1, self.spawn_cloud, True, True),
            "floor": Timer(0.5, self.spawn_floor, True, True),
            "floor_lines": Timer(0.1, self.spawn_floor1, True, True),
            "enemy": Timer(7.1, self.spawn_enemy, True, True),
        }

        self.font = load_font(
            r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\fonts\RETRO_SPACE.ttf")
        self.score = Score(self.font)
        self.dino_pos = Vector2(POS_X, POS_Y)
        self.dino_jump_sound = load_sound(
            r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\audio\jump.wav")
        self.dino = Dino(self.assets["player_assets"], self.assets["player_jump"], self.dino_pos, self.dino_jump_sound)

    def import_asses(self):
        line_textures = []
        for _ in range(5):
            img = gen_image_color(random.randint(2, 8), random.randint(1, 3), GRAY)
            line_textures.append(load_texture_from_image(img))
            unload_image(img)  

        self.assets = {
            'player_assets': [load_texture(
                rf"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\dino\run{i}.png") for i
                              in range(2)],
            "player_jump": load_texture(
                r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\dino\jump.png"),
            "cacti": [load_texture(
                rf"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\cactii\cactus{i}.png")
                      for i in range(4)],
            "cloud": [load_texture(
                rf"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\clouds\cloud{i}.png")
                      for i in range(4)],
            "floor": [load_texture(
                rf"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\floor\floor{i}.png") for
                      i in range(4)],
            "enemy": [load_texture(
                rf"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\enemy\enemy{i}.png") for
                      i in range(2)],
            "floor_lines": line_textures
        }

    def spawn_enemy(self):
        sprite = MovingSprites(self.assets["enemy"], Vector2(1280, random.randint(300, 420)), 7.6)
        self.sprite_list.append(sprite)
        self.colission_check_list.append(sprite)

    def spawn_floor1(self):
        text = random.choice(self.assets["floor_lines"])
        sprite = MovingSprites(text, Vector2(1280, random.randint(620, 640)), 7.6)
        self.sprite_list.append(sprite)

    def spawn_floor(self):
        sprite = MovingSprites(random.choice(self.assets["floor"]), Vector2(1280, 520), 7.6)
        self.sprite_list.append(sprite)

    def spawn_cloud(self):
        sprite = MovingSprites(random.choice(self.assets["cloud"]), Vector2(1280, random.randint(10, 200)), 4.4)
        self.sprite_list.append(sprite)

    def spawn_obstacle(self):
        sprite = MovingSprites(random.choice(self.assets["cacti"]), Vector2(1200, 480), 7.6)
        self.sprite_list.append(sprite)
        self.colission_check_list.append(sprite)

    def collission_check(self):
        player_circle = self.dino.get_colission_circle()
        if not player_circle:
            return

        for sprite in self.colission_check_list:
            obstacle_circle = sprite.get_colission_circle()
            if obstacle_circle:
                if check_collision_circles(
                        Vector2(player_circle[0], player_circle[1]), player_circle[2],
                        Vector2(obstacle_circle[0], obstacle_circle[1]), obstacle_circle[2]
                ):
                    close_window()
                    exit()

    def update(self, dt):
        self.dino.update(dt)

        for timer in self.timers.values():
            timer.update()

        for sprite in self.sprite_list:
            sprite.update(dt * 129)

        self.sprite_list = [s for s in self.sprite_list if s.pos.x > -150]
        self.colission_check_list = [s for s in self.colission_check_list if s.pos.x > -150]

        self.collission_check()

    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)

        for sprite in self.sprite_list:
            sprite.draw()

        draw_line_ex(Vector2(0, line_pos), Vector2(1280, line_pos), 10.5, GRAY)
        self.dino.draw()
        self.score.draw()

        end_drawing()

    def run(self):
        while not window_should_close():
            dt = get_frame_time()
            self.update(dt)
            self.draw()

        close_audio_device()
        close_window()


if __name__ == "__main__":
    game = Game()
    game.run()