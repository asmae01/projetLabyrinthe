import pygame
pygame.init()
myfont = pygame.font.SysFont('Helvetic', 20) #font de style
son = pygame.mixer.Sound("click.wav") #son du clique
fenetre=pygame.display.set_mode((1000,600)) #objet fentre principale
back=pygame.image.load("img/bg_zombie.jpg").convert() #image d'arriere plan
back=pygame.transform.scale(back, (1200,700)) #adjuster les dimention de l'image de backGround pour le fenêtre principale
fenetre.blit(back,(-20,0)) #applquer l'image d
width=fenetre.get_width()
height=fenetre.get_height()
fondexit=pygame.image.load("img/exit.jpeg").convert_alpha()
fondhelp=pygame.image.load("img/help.jpeg").convert_alpha()
fondstart=pygame.image.load("img/start.jpeg").convert_alpha()
fondhome=pygame.image.load("img/exit.jpeg").convert_alpha()
fondtext=pygame.image.load("img/txt_help.png").convert_alpha()
button_start= pygame.Rect(380, 100, 200, 50)
button_help= pygame.Rect(380, 250, 200, 50)
button_exit= pygame.Rect(380, 400, 200, 50)
button_home= pygame.Rect(700, 500, 200, 50)
#win button and fond
fondenext=pygame.image.load("img/next.png").convert_alpha()
button_next=pygame.Rect(590, 400, 200, 50)
fondexit1=pygame.image.load("img/exit.jpeg").convert_alpha()
button_exit1=pygame.Rect(200, 400, 200, 50)
#lose button and fond
fondreply=pygame.image.load("img/REPLAY.png").convert_alpha()
button_reply=pygame.Rect(590, 400, 200, 50)
