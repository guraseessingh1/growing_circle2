import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)

#filling background colour of the screen
screen.fill(white)
pygame.display.update()

#creating circle classdispl
class Circle():
    def __init__(self,color,pos,radius,width=0):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_width = width   
        self.circle_surface = screen 
        self.circle_radius = radius  

    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_pos,self.circle_radius,self.circle_width)

    def grow(self):
        self.circle_radius += 20
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_pos,self.circle_radius,self.circle_width)

circle1 =  Circle(red,(250,250),50,4)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(white)
            circle1.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill(white)
            circle1.grow()
            pygame.display.update()
            







        

