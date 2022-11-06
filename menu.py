import pygame, sys
from button import Button

pygame.init()

WIDTH = 1280
HEIGHT = 720

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))


def get_font(size):
    return pygame.font.Font("assets/earthquakemf.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        SCREEN.blit(BG, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()


        OPTIONS_TEXT = get_font(85).render("GAME OPTIONS:", True, "#80091b")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPEN_GAME_BUTTON = Button(pos=(640, 250),
                             text_input="OPEN", font=get_font(60), base_color="#ffffff", hovering_color="Black")
        SAVE_GAME_BUTTON = Button(pos=(640, 400),
                                  text_input="SAVE", font=get_font(60), base_color="#ffffff",
                                  hovering_color="Black")

        OPTIONS_BACK = Button(pos=(640, 600),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        for button in [OPEN_GAME_BUTTON, SAVE_GAME_BUTTON, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPEN_GAME_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    options()
                if SAVE_GAME_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    options()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#80091b")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(pos=(640, 250),
                            text_input="PLAY", font=get_font(75), base_color="#ffffff", hovering_color="Black")
        OPTIONS_BUTTON = Button(pos=(640, 400),
                            text_input="OPTIONS", font=get_font(75), base_color="#ffffff", hovering_color="Black")
        QUIT_BUTTON = Button(pos=(640, 550),
                            text_input="QUIT", font=get_font(75), base_color="#ffffff", hovering_color="Black")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()