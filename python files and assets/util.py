import pygame
from asset_var import *

# image load for button 160x160 is good for object,
def image_load(img_name,img_scale):
    image = pygame.image.load(img_name) 
    image = pygame.transform.scale(image,img_scale)
    return image

# objects

# render theme
def render_theme(screen, font, text):
    img = font.render(text, True, (0,0,0))
    screen.blit(img, (int(SCREEN_WIDTH/2 - img.get_width()/2),(int(SCREEN_HEIGHT/2 - img.get_height()/2))))

# render text 
def render_text(screen, font, text, y_pos):
    img = font.render(text, True, (0,0,0))
    screen.blit(img, (int(SCREEN_WIDTH/2 - img.get_width()/2),(y_pos- img.get_height()/2)))

def render_objecttext(screen, font, text, x_pos, y_pos):
    img = font.render(text, True, (0,0,0))
    screen.blit(img, (int(x_pos - img.get_width()/2),(y_pos - img.get_height()/2)))





class Button():
    def __init__(self, x_pos, y_pos, ori_img, hover_img):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ori_img = ori_img
        self.hover_img = hover_img
        self.image = ori_img
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen, x_p, y_p):
        if (x_p in range(self.rect.left, self.rect.right)) and (y_p in range(self.rect.top, self.rect.bottom)):
            self.image = self.hover_img
        else:
            self.image = self.ori_img
        screen.blit(self.image, self.rect)

    def checkInput(self, x_p, y_p):
        if (x_p in range(self.rect.left, self.rect.right)) and (y_p in range(self.rect.top, self.rect.bottom)):
            return True
        else:
            return False