# Test commit
import pygame

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 400
win = pygame.display.set_mode((300,400))
pygame.display.set_caption('PP Paint')

class Canvas:
    def __init__(self):
        self.rect = pygame.Rect(0,0,300,300)
        self.color = (255,255,0)
        self.tool = 'brush'
        self.colorMatrix = [[(255,255,255) for i in range(30)] for j in range(30)]
    def draw(self):
        pygame.draw.rect(win,self.color,self.rect)
        for i in range(0,300,10):
            for j in range(0,300,10):
                pygame.draw.rect(win,self.colorMatrix[int(j/10)][int(i/10)],(i,j,10,10))
                pygame.draw.line(win,(0,0,0),(i,0),(i,300))
                pygame.draw.line(win,(0,0,0),(0,j),(300,j))
    def setTool(self, tool):
        self.tool = tool

    def update(self):
        coords = pygame.mouse.get_pos()
        # print(coords[1] > self.rect.height + self.rect.top)
        print(coords)
        if coords[1] > self.rect.height + self.rect.top or coords[0] > SCREEN_WIDTH or coords[1] < 0 or coords[1] > SCREEN_HEIGHT or coords[0] < 0:
            return
        if self.tool == 'brush':
            if pygame.mouse.get_pressed()[0] == 1:
                self.colorMatrix[int(coords[1]/10)][int(coords[0]/10)] = self.color
        elif self.tool == 'eraser':
            if pygame.mouse.get_pressed()[0] == 1:
                self.colorMatrix[int(coords[1]/10)][int(coords[0]/10)] = (255,255,255)

canvas = Canvas()
class Toolbar:
    def __init__(self):
        self.rect = pygame.Rect(0,300,300,100)
        self.color = (50,50,50)
        self.tools = {
            "brush": {
                "rect": pygame.Rect(0,300,40,40),
                "color": (0,0,255),
                "active": True,
                "activate":  lambda : canvas.setTool('brush')
            },
            "eraser": {
                "rect": pygame.Rect(40,300,40,40),
                "color": (0,255,0),
                "active": True,
                "activate":  lambda : canvas.setTool('eraser')
            }
        }
    
    def draw(self):
        #TODO: Draw the toolbar separator here
        pygame.draw.rect(win,self.color,self.rect)
        for key, tool in self.tools.items():
            pygame.draw.rect(win, tool["color"], tool["rect"])

    def update(self):
        coords = pygame.mouse.get_pos()
        # print(coords[1] > self.rect.height + self.rect.top)
        print(coords)
        if coords[1] < self.rect.top or coords[1] > self.rect.height + self.rect.top or coords[0] > SCREEN_WIDTH or coords[1] < 0 or coords[1] > SCREEN_HEIGHT or coords[0] < 0:
            return
        if pygame.mouse.get_pressed()[0] == 1:
            if coords[0] <= 40 and coords[1] <= 340 and coords[1] > 300:
                self.tools["brush"]["active"] = True
                self.tools["brush"]["activate"]()
            elif coords[0] > 40 and coords[0] <= 80 and coords[1] <= 340 and coords[1] >= 300:
                self.tools["eraser"]["active"] = True
                self.tools["eraser"]["activate"]()
            else:
                self.tools["brush"]["active"] = False
                self.tools["eraser"]["active"] = False
                canvas.tool = "none"
        


toolbar = Toolbar()
run = True
while run:
    win.fill((255,255,255))
    canvas.draw()
    toolbar.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    canvas.update()
    toolbar.update()
    pygame.display.update()
    