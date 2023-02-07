import pygame
from random import choice, randint

def print_image(img_list) -> None:
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)

def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)

    rect = surface.get_rect(center=position)

    return [image, surface, rect]

def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def calculate_player_movement(keys):
    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    if keys[pygame.K_d]:
        delta_x += speed
    
    return [delta_x, delta_y]

def limit_position(position):
    x, y = position

    # zadanie domowe
    x = max(20, min(x, SCREEN_WIDTH - 20))
    y = max(20, min(y, SCREEN_HEIGHT - 20))

    return [x, y]

def generate_bonus_object():
    image_name = choice(bonus_images)

    x = randint(0, SCREEN_WIDTH)
    y = randint(0, SCREEN_HEIGHT)

    position = [x, y]

    new_obj = load_image(image_name, position)
    bonus_objects.append(new_obj)

def print_bonus_objects():
    for obj in bonus_objects:
        print_image(obj)

def check_collisions():
    rect_player = player[2]

    for i in range(len(bonus_objects) - 1, -1, -1):
        obj = bonus_objects[i]
        rect = obj[2]
        if rect.colliderect(rect_player):
            bonus_objects.pop(i)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Pierwsza Gra')

game_status = True
clock = pygame.time.Clock()

player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('player.png', player_pos)
background_color = (9, 42, 121)

bonus_images = [
    'bonus_1.png',
    'bonus_2.png',
    'bonus_3.png'
]

bonus_objects = []
frames_count = 0

while game_status:
    events = pygame.event.get()

    for event in events:
        # print(event)

        if event.type == pygame.QUIT:
            game_status = False

    pressed_keys = pygame.key.get_pressed()

    delta_x, delta_y = calculate_player_movement(pressed_keys)
    player_pos[0] += delta_x
    player_pos[1] += delta_y
    player_pos = limit_position(player_pos)

    player = set_position_image(player, player_pos)

    screen_surface.fill(background_color)

    print_image(player)
    
    if frames_count % (FPS * 1) == 0:
        generate_bonus_object()
    
    check_collisions()
    print_bonus_objects()

    pygame.display.update()

    clock.tick(FPS)

    frames_count += 1

pygame.quit()
quit()