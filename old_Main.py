import pygame
import sys
import numpy as np

pygame.init()

class chessgame:
    def __init__(self):
        self.FPS = 30
        self.screen = pygame.display.set_mode((600, 600))
        self.location = []

        #self.background_image = [pygame.image.load("image/green.png"), pygame.image.load("image/white.png")]

        self.black_bishop = pygame.image.load("image/black_bishop.png")
        self.black_king = pygame.image.load("image/black_king.png")
        self.black_knight = pygame.image.load("image/black_knight.png")
        self.black_pawn = pygame.image.load("image/black_pawn.png")
        self.black_rook = pygame.image.load("image/black_Rook.png")
        self.black_queen = pygame.image.load("image/black_queen.png")

        self.white_bishop = pygame.image.load("image/white_bishop.png")
        self.white_king = pygame.image.load("image/white_king.png")
        self.white_knight = pygame.image.load("image/white_knight.png")
        self.white_pawn = pygame.image.load("image/white_pawn.png")
        self.white_rook = pygame.image.load("image/white_Rook.png")
        self.white_queen = pygame.image.load("image/white_queen.png")

        self.black_pawn_x = [0,1,2,3,4,5,6,7]
        self.black_pawn_y = [1] * 8
        self.white_pawn_x = [0,1,2,3,4,5,6,7]
        self.white_pawn_y = [6] * 8

        self.black_bishop_x = [2,5]
        self.black_bishop_y = [0] * 2
        self.white_bishop_x = [2,5]
        self.white_bishop_y = [7] * 2

        self.black_knight_x = [1, 6]
        self.black_knight_y = [0] * 2
        self.white_knight_x = [1, 6]
        self.white_knight_y = [7] * 2

        self.black_rook_x = [0, 7]
        self.black_rook_y = [0] * 2
        self.white_rook_x = [0, 7]
        self.white_rook_y = [7] * 2

        self.black_king_x = 3
        self.black_king_y = 0
        self.white_king_x = 3
        self.white_king_y = 7

        self.black_queen_x = 4
        self.black_queen_y = 0
        self.white_queen_x = 4
        self.white_queen_y = 7

    def backgroud(self):
        self.location = []
        background_x = 0
        background_y = 0
        color1 = [(0,0,0),(255,255,255)]
        color = 1
        for i in range(8):
            for j in range(8):
                self.location.append(pygame.draw.rect(self.screen, color1[color],(background_x, background_y, 75, 75)))
                background_x += 75
                if color == 1:
                    color -= 1
                else:
                    color += 1
            if color == 1:
                color -= 1
            else:
                color += 1
            background_x = 0
            background_y += 75

    def chesspiece(self):
        for i in range(8): # 폰
            self.screen.blit(self.white_pawn,(self.white_pawn_x[i]*75,self.white_pawn_y[i]*75))
            self.screen.blit(self.black_pawn,(self.black_pawn_x[i]*75,self.black_pawn_y[i]*75))
        for i in range(2): # 비숍,나이트,룩
            self.screen.blit(self.black_bishop,(self.black_bishop_x[i]*75,self.black_bishop_y[i]*75))
            self.screen.blit(self.white_bishop, (self.white_bishop_x[i]*75, self.white_bishop_y[i]*75))
            self.screen.blit(self.black_knight,(self.black_knight_x[i]*75,self.black_knight_y[i]*75))
            self.screen.blit(self.white_knight, (self.white_knight_x[i]*75, self.white_knight_y[i]*75))
            self.screen.blit(self.black_rook,(self.black_rook_x[i]*75,self.black_rook_y[i]*75))
            self.screen.blit(self.white_rook, (self.white_rook_x[i]*75, self.white_rook_y[i]*75))

        self.screen.blit(self.black_king,(self.black_king_x*75,self.black_king_y*75)) #검은 킹
        self.screen.blit(self.white_king,(self.white_king_x*75, self.white_king_y*75))#하얀 킹

        self.screen.blit(self.black_queen,(self.black_queen_x*75,self.black_queen_y*75))#검은 퀸
        self.screen.blit(self.white_queen, (self.white_queen_x*75, self.white_queen_y*75))#하얀 퀸

    def click(self,pos):
        if self.location[0].collidepoint(pos):
            print("[0,0]")
            self.move("white","pawn",0,-1,1)

    def move(self,color,piece,x,y,*a):
        if color == "black":
            print("black")
            if piece == "pawn":
                self.black_pawn_x[a[0]] += x
                self.black_pawn_y[a[0]] += y
            elif piece == "knight":
                self.black_knight_x[a[0]] += x
                self.black_knight_y[a[0]] += y
            elif piece == "bishop":
                self.black_bishop_x[a[0]] += x
                self.black_bishop_y[a[0]] += y
            elif piece == "rook":
                self.black_rook_x[a[0]] += x
                self.black_rook_y[a[0]] += y
            elif piece == "king":
                self.black_king_x += x
                self.black_king_y += y
            elif piece == "queen":
                self.black_queen_x += x
                self.black_queen_y += y
        else:
            if piece == "pawn":
                self.white_pawn_x[a[0]] += x
                self.white_pawn_y[a[0]] += y
            elif piece == "knight":
                self.white_knight_x[a[0]] += x
                self.white_knight_y[a[0]] += y
            elif piece == "bishop":
                self.white_bishop_x[a[0]] += x
                self.white_bishop_y[a[0]] += y
            elif piece == "rook":
                self.white_rook_x[a[0]] += x
                self.white_rook_y[a[0]] += y
            elif piece == "king":
                self.white_king_x += x
                self.white_king_y += y
            elif piece == "queen":
                self.white_queen_x += x
                self.white_queen_y += y

    def check(self,x,y,x_1,y_1):
        pass



    def show(self):
        self.backgroud()
        self.chesspiece()

    def main(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.click(pos)
            self.show()
            pygame.display.flip()

if __name__ == "__main__":
    chessgame().main()