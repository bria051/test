import pygame
from map import get_pos_from_number

grid_size = 90

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)

class Draw(object):
    def __init__(self, surface):
        white_img = pygame.image.load('./image/white.png')
        black_img = pygame.image.load('./image/black.png')
        board_img = pygame.image.load('./image/t_by_t.png')
        self.white_img = pygame.transform.scale(white_img, (grid_size, grid_size))
        self.black_img = pygame.transform.scale(black_img, (grid_size, grid_size))
        self.last_w_img = pygame.image.load('./image/white_a.png')
        self.last_b_img = pygame.image.load('./image/black_a.png')
        self.board_img = pygame.transform.scale(board_img, (300, 300))
        self.surface = surface
        self.font = pygame.font.Font("freesansbold.ttf", 100)

    def init_game(self):
        self.draw_board()
        self.draw_font()

    def draw_board(self):
        self.surface.blit(self.board_img, (0, 0))

    def draw_font(self):
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('2 Players', True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (400, 100)
        self.surface.blit(textSurfaceObj, textRectObj)

    def draw_font_t(self):
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('user vs com', True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (425, 200)
        self.surface.blit(textSurfaceObj, textRectObj)

    def draw_stone(self, number,temp):
        img = [self.black_img, self.white_img, self.last_b_img, self.last_w_img]
        x, y = get_pos_from_number(number)
        if(temp == 'O'):
            num = 0
        else:
            num = 1
        self.surface.blit(img[num], (x, y))