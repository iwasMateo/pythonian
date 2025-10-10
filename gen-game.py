import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
def getDistance(object1, object2):
    x1, y1 = object1.x, object1.y
    x2, y2 = object2.x, object2.y
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
class Dot:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
    def pos(self):
        print("Position:", self.x, self.y)
    def moveTowards(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            dx /= dist
            dy /= dist

            self.x += dx * self.speed
            self.y += dy * self.speed

Body = Dot(100, 100, 40, 40, RED, 1)
Ankle = Dot(150, 150, 20, 20, BLUE, 5)
while running:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            running=False
    screen.fill(WHITE)
    
    keys = pygame.key.get_pressed()
    Body.draw(screen)
    Ankle.draw(screen)
    
    # print("Distance:", getDistance(Body, Ankle))
    if getDistance(Body, Ankle) < 100:
        Ankle.move(keys)
    else:
        while getDistance(Body, Ankle) > 50:
            Body.moveTowards(Ankle)



    pygame.display.flip()
    clock.tick(30)

pygame.quit()