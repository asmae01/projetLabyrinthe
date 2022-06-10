import pygame
from constantes import *
from maze_generator import *
import time


def is_collide(x, y, player_rect, walls_collide_list):
    tmp_rect = player_rect.move(x, y)
    if tmp_rect.collidelist(walls_collide_list) == -1:
        return False
    return True


def is_game_over(TILE, player_rect):
    global time, score
    if time < 0:
        pygame.time.wait(700)
        player_rect.center = TILE // 2, TILE // 2
        time, score = 20, 0


def start(TILE, time):
    direction = (0, 0)
    cols, rows = WIDTH // TILE, HEIGHT // TILE
    # timer, score
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    score = 0

    FPS = 60
    game_surface = pygame.Surface(RESOLUTION)
    surface = pygame.display.set_mode((WIDTH, HEIGHT + 100))
    clock = pygame.time.Clock()

    # images
    bg_game = pygame.image.load('img/bg_zombie.jpg').convert()
    bg = pygame.image.load('img/bg.png').convert()

    # get maze
    maze = generate_maze(cols, rows)

    # player settings
    player_speed = 10
    player_img = pygame.image.load('img/zombie.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_LEFT, 'd': pygame.K_RIGHT, 'w': pygame.K_UP, 's': pygame.K_DOWN}

    # le but
    but = pygame.image.load("img/end.png").convert_alpha()
    rectangleDeBut = pygame.transform.scale(but, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    but_x = WIDTH - TILE
    but_y = HEIGHT - TILE

    # collision list
    walls_collide_list = sum([cell.get_rects(TILE) for cell in maze], [])


    # fonts
    font = pygame.font.SysFont('Impact', 40)
    text_font = pygame.font.SysFont('Impact', 40)

    while True:
        surface.blit(bg, (0, HEIGHT))
        surface.blit(game_surface, (0, 0))
        game_surface.blit(bg_game, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.USEREVENT:
                time -= 1

        # conrole et mouvement de joueure
        pressed_key = pygame.key.get_pressed()
        for key, key_value in keys.items():
            if pressed_key[key_value] and not is_collide(*directions[key], player_rect, walls_collide_list):
                direction = directions[key]
                break
        if not is_collide(*direction, player_rect, walls_collide_list):
            player_rect.move_ip(direction)

        # dessiner le labyrinthe
        [cell.draw(game_surface, TILE) for cell in maze]

        # verifie si le joueur a attient le but
        if (player_rect[0] == WIDTH - TILE + 4) and (player_rect[1] == HEIGHT - TILE + 4):
            game_win(time)
        # verifie si le temps est ecoule
        if time < 0 and not ((player_rect[0] == WIDTH - TILE + 4) and (player_rect[1] == HEIGHT - TILE + 4)):
            game_over()
        # draw player
        game_surface.blit(player_img, player_rect)

        # draw le but
        game_surface.blit(rectangleDeBut, (but_x, but_y))
        # time and score affichage
        if ((player_rect[0] != WIDTH - TILE + 4) or (player_rect[1] != HEIGHT - TILE + 4)) and time >= 0:
            surface.blit(text_font.render('TIME :', True, pygame.Color('orangered')), ((WIDTH // 2) - 70, HEIGHT + 15))
            surface.blit(font.render(f'{time}', True, pygame.Color('orangered')), ((WIDTH // 2) + 30, HEIGHT + 15))

        # print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)


def game_over():
    # fonts
    font = pygame.font.SysFont('Impact', 40)
    text_font = pygame.font.SysFont('Impact', 100)
    fenetre.blit(back, (-20, 0))
    fenetre.blit(text_font.render('GAME OVER!', True, pygame.Color('orangered')),
                 ((WIDTH // 2) - 240, HEIGHT // 2 - 100))
    fenetre.blit(fondreply, (590, 400))
    fenetre.blit(fondexit1, (200, 400))
    gerer_mouse_over()


def gerer_mouse_over():
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:  # UP
        mouse_pos = pygame.mouse.get_pos()

        if button_reply.collidepoint(mouse_pos):
            son.play()
            start(100, 20)
        if button_exit1.collidepoint(mouse_pos):
            son.play()
            time.sleep(0.2)
            exit()
global test
test = True
def game_win(time):
    global test
    if test == True:
        global t
        t = time
        test = False

    font = pygame.font.SysFont('Impact', 40)
    text_font = pygame.font.SysFont('Impact', 100)
    text_font1 = pygame.font.SysFont('Impact', 25)
    fenetre.blit(back, (-20, 0))
    fenetre.blit(text_font.render('YOU WIN!', True, pygame.Color('orangered')), ((WIDTH // 2) - 190, HEIGHT // 2 - 100))
    fenetre.blit(text_font1.render('You are scored : ' + str(100 - t), True, pygame.Color('orangered')), ((WIDTH // 2 + 20) - 100, HEIGHT // 2 + 50))
    fenetre.blit(fondenext, (590, 400))
    fenetre.blit(fondexit1, (200, 400))
    gerer_mouse_win()


def gerer_mouse_win():
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:  # UP
        mouse_pos = pygame.mouse.get_pos()

        if button_next.collidepoint(mouse_pos):
            # hna fin z7lna l3ibat
            son.play()
            start(50, 40)
        if button_exit1.collidepoint(mouse_pos):
            son.play()
            time.sleep(0.2)
            exit()


def home():
    fenetre.blit(back, (-20, 0))
    fenetre.blit(fondstart, (380, 100))
    fenetre.blit(fondhelp, (380, 250))
    fenetre.blit(fondexit, (380, 400))
    gerer_mouse_home()


def help():
    fenetre.blit(back, (-20, 0))
    fenetre.blit(fondhome, (700, 500))
    fenetre.blit(fondtext, (100, 100))
    gerer_mouse_help()


def gerer_mouse_home():
    global afficher

    mouse = pygame.mouse.get_pressed()
    if mouse[0]:  # UP
        mouse_pos = pygame.mouse.get_pos()

        if button_start.collidepoint(mouse_pos):
            son.play()
            afficher = start(100, 20)

        if button_help.collidepoint(mouse_pos):
            son.play()
            afficher = help
        if button_exit.collidepoint(mouse_pos):
            son.play()
            time.sleep(0.2)
            exit()


def gerer_mouse_help():
    global afficher

    mouse = pygame.mouse.get_pressed()
    if mouse[0]:  # UP
        mouse_pos = pygame.mouse.get_pos()

        if button_home.collidepoint(mouse_pos):
            son.play()
            afficher = home


def quiter():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
