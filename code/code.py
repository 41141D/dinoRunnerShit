import raylib as rl
from pyray import *
import random
init_window(1280,720,"dinoRunnerShit")
init_audio_device()
custom_font = load_font(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\fonts\RETRO_SPACE.ttf")
POS_X = 30
CACTUS_COLOR = GREEN
POS_Y = 530
set_target_fps(75)
dino_text = load_texture("C:/Users/TheG0/OneDrive/Desktop/drive-download-20260820T164053Z-1-001/assets/dino/eggno.png")
cactus_text = load_texture(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\cactii\cactus0.png")
cactus_text2=load_texture(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\cactii\cactus1.png")
cactus_text3 = load_texture(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\cactii\cactus2.png")
cactus_text4= load_texture(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\assets\cactii\cactus3.png")
jump_sound = load_sound(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\audio\jump.wav")
music = load_music_stream(r"C:\Users\TheG0\OneDrive\Desktop\drive-download-20260820T164053Z-1-001\audio\music.mp3")
st_ps = Vector2(10,100)
end_ps = Vector2(500,100)
dino_rotation = 0
play_music_stream(music)
velocity = 0
gravity = 0.8
dino_pos = Vector2(POS_X,POS_Y)
line_pos = 615
is_grounded = True
cacti_text_lst = [cactus_text,cactus_text2,cactus_text3,cactus_text4]
cacti_list = []
cactus_timer = 0
cactus_interval = 3
while True:
    cactus_timer+=0.5
    if cactus_timer >= cactus_interval:
        cactus_timer = 0
        cacti_list.append(Vector2(1280,line_pos))

    for cactus_pos in cacti_list:
        cactus_pos.x -= 8

    velocity += gravity
    begin_drawing()
    update_music_stream(music)
    clear_background(RAYWHITE)
    draw_line_ex(Vector2(0,line_pos+80),Vector2(1280,line_pos + 80),10.5,BROWN)

    draw_texture_ex(dino_text,dino_pos,dino_rotation,0.1,PURPLE)
    for cactus_pos in cacti_list:
        draw_texture_ex(random.choice(cacti_text_lst),cactus_pos , 0, 3, CACTUS_COLOR)




    draw_text_ex(custom_font,f"SCORE : {int(get_time())}",Vector2(540,10),40,3,RED)

    dino_pos.y+=velocity
    if dino_pos.y > 615:
        dino_pos.y = 615
        velocity = 0
        is_grounded = True
    if is_key_pressed(rl.KEY_W) and is_grounded:
        play_sound(jump_sound)
        dino_rotation = +6
        velocity -=19
        is_grounded = False
    if is_key_released(rl.KEY_W):
        dino_rotation = 0
        POS_Y = 530
    if is_key_down(rl.KEY_D):
        dino_pos.x += 10
    if is_key_down(rl.KEY_A):
        dino_pos.x -= 10


    if check_collision_recs(Rectangle(dino_pos.x,dino_pos.y,dino_text.width*0.1,dino_text.height*0.1),Rectangle(cactus_pos.x,cactus_pos.y,cactus_text.width * 3,cactus_text.height * 3)):
        CACTUS_COLOR = RED
    else:
        CACTUS_COLOR = GREEN
    end_drawing()
    if is_key_pressed(rl.KEY_ESCAPE):
        break