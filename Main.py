import pygame
import pprint
import sys
import numpy as np

pygame.init()

class chessgame:
    def __init__(self):
        self.FPS = 30
        self.screen = pygame.display.set_mode((600, 600))
        self.font = pygame.font.SysFont("notosanscjkkr", 30)
        self.clicked = False
        self.click_x,self.click_y = 0,0
        self.turn = False #True : 검은색 False :하얀색

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

        self.board = np.zeros((8,8))
        # 1 : 폰 2 : 룩 3 : 나이트 4: 비숍 5: 킹 6 : 퀸
        # 음수 : 화이트

        #폰
        for i in range(8):
            self.board[1][i] = 1
            self.board[6][i] = -1

        #룩
        self.board[0][0] = 2
        self.board[0][7] = 2
        self.board[7][0] = -2
        self.board[7][7] = -2

        #나이트
        self.board[0][1] = 3
        self.board[0][6] = 3
        self.board[7][1] = -3
        self.board[7][6] = -3

        #비숍
        self.board[0][2] = 4
        self.board[0][5] = 4
        self.board[7][2] = -4
        self.board[7][5] = -4

        #킹
        self.board[0][3] = 5
        self.board[7][3] = -5

        #퀸
        self.board[0][4] = 6
        self.board[7][4] = -6

        self.location = [[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

        self.canmove = [[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

        background_x = 0
        background_y = 0
        color1 = [(0, 0, 0), (255, 255, 255)]
        color = 1
        for i in range(8):
            for j in range(8):
                self.location[i][j] = pygame.draw.rect(self.screen, color1[color], (background_x, background_y, 75, 75))
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

    def backgroud(self):
        background_x = 0
        background_y = 0
        color1 = [(0,0,0),(255,255,255)]
        color = 1
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen, color1[color],(background_x, background_y, 75, 75))
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
        #print(len(self.location))

    def chesspiece(self):
        #pprint.pprint(self.board)
        for x in range(8):
            for y in range(8):
                self.show(x, y)

    def click(self,pos):
        for i in range(8):
            for j in range(8):
                if self.location[i][j].collidepoint(pos):
                    print(f"[{i},{j}]")
                    if self.board[i][j] == 0 and not(self.clicked):
                        print("공백")
                        return
                    if self.clicked:
                        if self.board[self.click_x][self.click_y] > 0 and not (self.turn) or self.board[self.click_x][self.click_y] < 0 and self.turn:
                            print("자신의 턴이 아님")
                            return
                    elif self.board[i][j] > 0 and not(self.turn) or self.board[i][j] < 0 and self.turn:
                        print("자신의 턴이 아님")
                        return
                    if not(self.clicked):
                        self.click_x,self.click_y = i,j
                    x,y = i,j
        # turn True = 검은색 Fasle = 하얀색  양수 = 블랙  음수 = 화이트
        if self.clicked:
            if self.click_x == x and self.click_y == y:
                print("똑같은 곳 클릭")
                return
            self.move(self.click_x,self.click_y,x,y)
            self.clicked = False
            self.click_x = 0
            self.click_y = 0
        else:
            self.clicked = True

    def show(self,x,y):# 1 : 폰 2 : 룩 3 : 나이트 4: 비숍 5: 킹 6 : 퀸
        if self.board[x][y] == 0:
            #print("공백")
            return
        elif self.board[x][y] > 0:
            #print("블랙")
            if self.board[x][y] == 1:
                #print("폰")
                self.screen.blit(self.black_pawn,(y*75,x*75))
            elif self.board[x][y] == 2:
                #print("룩")
                self.screen.blit(self.black_rook, (y * 75, x * 75))
            elif self.board[x][y] == 3:
                #print("나이트")
                self.screen.blit(self.black_knight, (y * 75, x * 75))
            elif self.board[x][y] == 4:
                #print("비숍")
                self.screen.blit(self.black_bishop, (y * 75, x * 75))
            elif self.board[x][y] == 5:
                #print("킹")
                self.screen.blit(self.black_king,(y*75,x*75))
            elif self.board[x][y] == 6:
                #print("퀸")
                self.screen.blit(self.black_queen, (y * 75, x * 75))
        else :
            #print("화이트")
            if self.board[x][y]*-1 == 1:
                #print("폰")
                self.screen.blit(self.white_pawn, (y * 75, x * 75))
            elif self.board[x][y]*-1 == 2:
                #print("룩")
                self.screen.blit(self.white_rook, (y * 75, x * 75))
            elif self.board[x][y]*-1 == 3:
                #print("나이트")
                self.screen.blit(self.white_knight, (y * 75, x * 75))
            elif self.board[x][y]*-1 == 4:
                #print("비숍")
                self.screen.blit(self.white_bishop, (y * 75, x * 75))
            elif self.board[x][y]*-1 == 5:
                #print("킹")
                self.screen.blit(self.white_king, (y * 75, x * 75))
            elif self.board[x][y]*-1 == 6:
                #print("퀸")
                self.screen.blit(self.white_queen, (y * 75, x * 75))

    def movemake(self,x,y):
        print("x+1 = ",x+1,"x-1 = ",x-1,"y+1 = ",y+1,"y-1 = ",y-1)
        if abs(self.board[x][y]) == 6:
            if x+1 <= 7:
                self.canmove[x + 1][y] = 1
                if y+1 <= 7:
                    self.canmove[x + 1][y + 1] = 1
                if y-1 >=0:
                    self.canmove[x + 1][y - 1] = 1
            if x-1 >=0:
                self.canmove[x - 1][y] = 1
                if y+1 <= 7:
                    self.canmove[x - 1][y + 1] = 1
                    self.canmove[x][y + 1] = 1
                if y-1 >=0:
                    self.canmove[x - 1][y - 1] = 1
                    self.canmove[x][y - 1] = 1

            self.showmove()

    def showmove(self):
        for i in range(8):
            for j in range(8):
                if self.canmove[i][j] == 1:
                    pygame.draw.circle(self.screen, (190, 190, 190),
                                       (j * 75 + 37, i * 75 + 37), 10)
                self.canmove[i][j] = 0


    def move(self,x,y,new_x,new_y):
        self.board[new_x][new_y] = self.board[x][y]
        self.board[x][y] = 0
        self.turn = not(self.turn)

    def game(self):
        if self.turn: #검은색
            self.screen.blit(self.font.render("BLACK TURN", True, (50, 255, 255)), (250, 20))
        else: #하얀색
            self.screen.blit(self.font.render("WHITE TURN", True, (50, 255, 255)), (250, 20))

        black = 0
        white = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] > 0:
                    black += 1
                elif self.board[i][j] < 0:
                    white += 1
        if 6 in self.board:
            pass
            #print("검은 퀸 살아있음")
        else:
            self.screen.blit(self.font.render("WHITE WIN", True, (50, 255, 255)), (300, 250))
            #print("검은 퀸 죽음 흰색 이김")
        if -6 in self.board:
            pass
            #print("하얀 퀸 살아있음")
        else:
            self.screen.blit(self.font.render("BLACK WIN", True, (50, 255, 255)), (300, 250))
            #print("하얀 퀸 죽음 검은색 이김")
        #print(black,white)


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
            self.backgroud()
            self.chesspiece()
            self.movemake(self.click_x, self.click_y)
            self.game()

            pygame.display.flip()

if __name__ == "__main__":
    chessgame().main()