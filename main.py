from all import *
from constantes import *

RUNNING = True
afficher = home


def boucle_principale():
    while RUNNING:
        fenetre.fill((0, 0, 0))

        quiter()

        # Exécute la fonction affecté à afficher
        afficher()

        pygame.display.update()

    pygame.quit()


boucle_principale()
