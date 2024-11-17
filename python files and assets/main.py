# =============================
# Wolfjaw Game Jam
# Theme: Connect
# Desc.: 2 player causual game
# Auth.: akkilin
# =============================
import pygame
import pygame.locals
import sys
import time
import random
from asset_var import *
from util import *

# ===========================================
# Standard Initializations
# ===========================================
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# ===========================================
# Game state variables
# ===========================================
# Init. first topic and list
theme_index = random.randint(0, len(phrases) - 1)
current_phrase = phrases[theme_index]
current_list = object_lists[theme_index]

player_choices = [None, None]  

# score system and connectivity streak not implemented

# ===========================================
# Different Scenes
# ===========================================

# main menu
def main_menu(current_phrase, current_list, player_choices):
    pygame.display.set_caption("banana smoothie")
    
    # Load button images and init the buttons 
    start_bimg = image_load("ori_start.png",menu_img_scale)
    start_bhover = image_load("hover_start.png",menu_img_scale) 
    exit_bimg = image_load("ori_exitbutton.png",menu_img_scale) 
    exit_bhover = image_load("hover_exitbutton.png",menu_img_scale) 
    start_button = Button(325, 300, start_bimg, start_bhover)
    exit_button = Button(475, 300, exit_bimg, exit_bhover);

    while True:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkInput(mouse_pos[0],mouse_pos[1]):
                    theme_transition(current_phrase, current_list, player_choices)
                if exit_button.checkInput(mouse_pos[0],mouse_pos[1]):
                    pygame.quit()
                    sys.exit()
        
        start_button.update(screen, mouse_pos[0],mouse_pos[1])
        exit_button.update(screen, mouse_pos[0],mouse_pos[1])
        pygame.display.flip()
        clock.tick(60)
        
# theme display and transition
def theme_transition(current_phrase, current_list, player_choices):
    pygame.display.set_caption(current_phrase)
    start_time = time.time()
    while (time.time()-start_time) < 3.0:
        screen.fill(WHITE)
        render_theme(screen, font, current_phrase)
        render_text(screen, font, str(int(4-(time.time()-start_time))), 200)
        pygame.display.flip()
        clock.tick(60)
    pick1(current_phrase, current_list, player_choices)

# player 1 pick; if doesn't pick -> main menu
def pick1(current_phrase, current_list, player_choices):
    pygame.display.set_caption("PICK!")
    start_time = time.time()
    choice_img = pygame.image.load("object_choice.png") 
    chover_img = pygame.image.load("hover_object_choice.png")
    # create buttons to select
    cbutton1 = Button(108, 400, choice_img, chover_img);
    cbutton2 = Button(303, 400, choice_img, chover_img);
    cbutton3 = Button(498, 400, choice_img, chover_img);
    cbutton4 = Button(693, 400, choice_img, chover_img);

    while (time.time()-start_time) < 10.3:
        screen.fill(WHITE)
        render_text(screen, font, current_phrase, 100)
        render_text(screen, font, str(int(11-(time.time()-start_time))), 50)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cbutton1.checkInput(mouse_pos[0],mouse_pos[1]):
                    player_choices[0] = current_list[0]
                    player_transition(current_phrase, current_list, player_choices)
                if cbutton2.checkInput(mouse_pos[0],mouse_pos[1]):
                    player_choices[0] = current_list[1]
                    player_transition(current_phrase, current_list, player_choices)
                if cbutton3.checkInput(mouse_pos[0],mouse_pos[1]):
                    player_choices[0] = current_list[2]
                    player_transition(current_phrase, current_list, player_choices)
                if cbutton4.checkInput(mouse_pos[0],mouse_pos[1]):
                    player_choices[0] = current_list[3]
                    player_transition(current_phrase, current_list, player_choices)
        
        
        mouse_pos = pygame.mouse.get_pos()
        cbutton1.update(screen, mouse_pos[0],mouse_pos[1])
        cbutton2.update(screen, mouse_pos[0],mouse_pos[1])
        cbutton3.update(screen, mouse_pos[0],mouse_pos[1])
        cbutton4.update(screen, mouse_pos[0],mouse_pos[1])
        # render the objects
        render_objecttext(screen, font, current_list[0], 108, 400)
        render_objecttext(screen, font, current_list[1], 303, 400)
        render_objecttext(screen, font, current_list[2], 498, 400)
        render_objecttext(screen, font, current_list[3], 693, 400)
        pygame.display.flip()
        clock.tick(60)
    main_menu(current_phrase, current_list, player_choices)

# player transition page; one computer
def player_transition(current_phrase, current_list, player_choices):
    pygame.display.set_caption("SWITCH PLAYERS!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_time = time.time()
                while (time.time()-start_time) < 3.0:
                    screen.fill(WHITE)
                    render_text(screen, font, str(int(4.0-(time.time()-start_time))), 100)
                    render_theme(screen, font, current_phrase)
                    pygame.display.flip()
                    clock.tick(60)
                pick2(current_phrase, current_list, player_choices)

        screen.fill(WHITE)
        render_theme(screen, font, current_phrase)
        render_text(screen, font, "Switch To Other Person!", 200)
        pygame.display.flip()
        clock.tick(60)

# player 2 pick; if doesn't pick -> player transition
def pick2(current_phrase, current_list, player_choices):
    pygame.display.set_caption("PICK!")
    start_time = time.time()
    choice_img = pygame.image.load("object_choice.png") 
    chover_img = pygame.image.load("hover_object_choice.png")
    # create buttons to select
    cbutton1 = Button(108, 400, choice_img, chover_img);
    cbutton2 = Button(303, 400, choice_img, chover_img);
    cbutton3 = Button(498, 400, choice_img, chover_img);
    cbutton4 = Button(693, 400, choice_img, chover_img);

    while (time.time()-start_time) < 10.3:
        screen.fill(WHITE)
        render_text(screen, font, current_phrase, 100)
        render_text(screen, font, str(int(11-(time.time()-start_time))), 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cbutton1.checkInput(mouse_pos[0],mouse_pos[1]):
                    player_choices[1] = current_list[0]
                    result_transition(current_phrase, current_list, player_choices)
                if cbutton2.checkInput(mouse_pos[0],mouse_pos[1]):
                    player_choices[1] = current_list[1]
                    result_transition(current_phrase, current_list, player_choices)
                if cbutton3.checkInput(mouse_pos[0],mouse_pos[1]):
                    player_choices[1] = current_list[2]
                    result_transition(current_phrase, current_list, player_choices)
                if cbutton4.checkInput(mouse_pos[0],mouse_pos[1]):
                    player_choices[1] = current_list[3]
                    result_transition(current_phrase, current_list, player_choices)
        
        mouse_pos = pygame.mouse.get_pos()
        cbutton1.update(screen, mouse_pos[0],mouse_pos[1])
        cbutton2.update(screen, mouse_pos[0],mouse_pos[1])
        cbutton3.update(screen, mouse_pos[0],mouse_pos[1])
        cbutton4.update(screen, mouse_pos[0],mouse_pos[1])
        # render the objects
        render_objecttext(screen, font, current_list[0], 108, 400)
        render_objecttext(screen, font, current_list[1], 303, 400)
        render_objecttext(screen, font, current_list[2], 498, 400)
        render_objecttext(screen, font, current_list[3], 693, 400)
        pygame.display.flip()
        clock.tick(60)
    player_transition(current_phrase, current_list, player_choices)

# result transition; timer because takes time for two people to get back to one computer
def result_transition(current_phrase, current_list, player_choices):
    pygame.display.set_caption("RESULTS?")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_time = time.time()
                while (time.time()-start_time) < 3.0:
                    screen.fill(WHITE)
                    render_text(screen, font, "Results in...", 275)
                    render_text(screen, font, str(int(4.0-(time.time()-start_time))), 325)
                    pygame.display.flip()
                    clock.tick(60)
                correctness_page(current_phrase, current_list, player_choices)

        screen.fill(WHITE)
        render_theme(screen, font, "Results?")
        pygame.display.flip()
        clock.tick(60)

# result page; ask replay or exit
def correctness_page(current_phrase, current_list, player_choices):
    if player_choices[0]==player_choices[1]:
        image = image_load("correct.png",(80,80))
    else:
        image = image_load("wrong.png",(80,80))

    # Load button images and init the buttons 
    start_bimg = image_load("ori_start.png",menu_img_scale)
    start_bhover = image_load("hover_start.png",menu_img_scale) 
    exit_bimg = image_load("ori_exitbutton.png",menu_img_scale) 
    exit_bhover = image_load("hover_exitbutton.png",menu_img_scale) 
    start_button = Button(325, 475, start_bimg, start_bhover)
    exit_button = Button(475, 475, exit_bimg, exit_bhover);

    while True:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkInput(mouse_pos[0],mouse_pos[1]):
                    theme_index = random.randint(0, len(phrases) - 1)
                    current_phrase = phrases[theme_index]
                    current_list = object_lists[theme_index]
                    player_choices = [None, None]
                    theme_transition(current_phrase, current_list, player_choices)
                if exit_button.checkInput(mouse_pos[0],mouse_pos[1]):
                    pygame.quit()
                    sys.exit()
        
        # screen stuff
        start_button.update(screen, mouse_pos[0],mouse_pos[1])
        exit_button.update(screen, mouse_pos[0],mouse_pos[1])
        render_objecttext(screen, font, "Person 1 said:", 200, 300)
        render_objecttext(screen, font, "Person 2 said:", 600, 300)
        render_objecttext(screen, font, player_choices[0], 200, 350)
        render_objecttext(screen, font, player_choices[1], 600, 350)
        screen.blit(image, (int(SCREEN_WIDTH/2 - image.get_width()/2),(200 - image.get_height()/2)))
        render_text(screen, font, "Replay?", 100)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main_menu(current_phrase, current_list, player_choices)
    pygame.quit()
    sys.exit()