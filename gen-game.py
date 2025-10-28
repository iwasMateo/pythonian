import pygame
import math
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Walking Ant")
clock = pygame.time.Clock()
running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
def getDistance(object1, object2): # make a function to get te distance between two things
    x1, y1 = object1.x, object1.y
    x2, y2 = object2.x, object2.y
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
def getMiddlex(object1, object2): # get x of a middle point in between two objects
    x1 = object1.x
    x2 = object2.x
    return ((x1 + x2) / 2)
def getMiddley(object1, object2): # # get x of a middle point in between two objects
    y1 = object1.y
    y2 = object2.y
    return ((y1 + y2) / 2)
class Middlepoint: # make a middle point
                   # dunno why i did this seperate from the "getMiddlex" and "getMiddley" functions
    def __init__(self, object1, object2):
        self.object1 = object1
        self.object2 = object2
    @property
    def x(self):
        return(self.object1.x+ self.object2.x)/2
    @property
    def y(self):
        return(self.object1.y+ self.object2.y)/2
class Dot: # make a playable dot
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def arrow_move(self, keys): # check for arrow keys and move accordingly
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
    def wasd_move(self, keys): # check for wasd keys and move accordingly
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
    def pos(self): # get position
        return( self.x, self.y)
    def moveTowards(self, target, move_speed): # move towards a target
        dx = target.x - self.x
        dy = target.y - self.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            dx /= dist
            dy /= dist

            self.x += dx * move_speed
            self.y += dy * move_speed
def normalPhysWalk(): # Give it a little bit of "Do not rip my legs off please"
    # When I am allowed to move
    if getDistance(Body, Ankle1) < 75: # and getDistance(Body, Ankle1) > 20:
        Ankle1.arrow_move(keys)
    else:
        Ankle1.moveTowards(Body, 1)
    if getDistance(Body, Ankle2) < 75: # and getDistance(Body, Ankle2) > 20:
        Ankle2.wasd_move(keys)
    # Making sure that the individual body parts don't get ripped to shreds
    else:
        Ankle2.moveTowards(Body, 1)
    if getDistance(Bodmid1, Foot1) > 10:
        Foot1.moveTowards(Bodmid1, 2*(getDistance(Bodmid1, Foot1)/10))
    if getDistance(Bodmid2, Foot2) > 10:
        Foot2.moveTowards(Bodmid2, 2*(getDistance(Bodmid2, Foot2)/10))
    if getDistance(Body, Anklemid) > 5:
        Body.moveTowards(Anklemid, 1)
foot1walked=0
foot1walk = False
foot2walked=0
foot2walk = False
def autoWalk(target):
    # Basically the point of the entire program lol
    global foot1walked, foot1walk, foot2walked, foot2walk # "import" some of the stuff necessary
    BodyTargetMid = Middlepoint(Body, target) # get the middle point of the target and the body
    # Old Version of the code that I wanted to preserve
    #if getDistance(Foot1, target) < getDistance(Foot2, target):
    #    print("Foot1 closer")
    #    foot1walk = False
    #    if foot2walked <= 30:
    #        foot2walk = True
    #        print("Foot2 walking")
    #    else:
    #        foot2walk = False
    #        foot2walked = 0
    #        print("Foot2 not walking")
    #else: 
    #    print("Foot1 closer")
    #    foot2walk = False
    #    if foot1walked <= 30:
    #        foot1walk = True
    #        print("Foot1 walking")
    #    else:
    #        foot1walk = False
    #        foot1walked = 0
    #        print("Foot1 not walking")
    #if foot1walk:
    #    if not foot1col == (175, 222, 209):
    #        Foot1.moveTowards(target, 1)
    #        foot1walked+=1
    if getDistance(Body, target) > 20: # if it's further away than basically there then it does that
        # The actual walk cycle (working this time)
        if foot1walk: # if foot1 is supposed to be walking
            if foot1walked <= 60: # if the foot has not walked 60 pixels yet then
                A = pygame.Vector2(Foot1.x, Foot1.y)
                B = pygame.Vector2(target.x, target.y)
                direction = (B - A).normalize()
                left_direction = direction.rotate(-90)
                final_point = B+left_direction*50
                Ankle1.moveTowards(final_point, 1)
                foot1walked += 1
                print("Foot1 successfully walking to target")
            else: # otherwise it's the other foots turn
                foot1walk = False
                foot1walked = 0
                print("Foot1 not walking")
        elif foot2walk: # if foot2 is supposed to be walking then
            if foot2walked <= 60:
                A = pygame.Vector2(Foot2.x, Foot2.y)
                B = pygame.Vector2(target.x, target.y)
                direction = (B - A).normalize()
                left_direction = direction.rotate(90)
                final_point = B+left_direction*50
                Ankle2.moveTowards(final_point, 1)
                foot2walked += 1
                print("Foot2 successfully walking to target")
            else:
                foot2walk = False
                foot2walked = 0
                print("Foot2 not walking")
        else: # if "not sure" then look which one should walk
            if getDistance(Foot1, target) < getDistance(Foot2, target):
                print("Foot1 closer")
                foot1walk = False
                foot2walk = True
                print("Foot2 walking")
            else:
                print("Foot2 closer")
                foot2walk = False
                foot1walk = True
                print("Foot1 walking")
    else:
        print("At target")
# All used Body parts
Body = Dot(100, 100, 12, BLACK, 1)
Ankle1 = Dot(150, 150, 8, RED, 5)
Ankle2 = Dot(50, 50, 8, GREEN, 5)
Foot1 = Dot(190, 190, 9, PURPLE, 5)
Foot2 = Dot(20, 20, 9, CYAN, 5)
target = Dot(400, 300, 5, RED, 0)
Anklemid = Middlepoint(Ankle1, Ankle2)
Bodmid1= Middlepoint(Body, Ankle1)
Bodmid2= Middlepoint(Body, Ankle2)
autowalk = True
last_toggle_time = 0 
# game loop
while running:
    buttons = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if buttons[0]:
            target.x, target.y = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            current_time = pygame.time.get_ticks()
            if current_time - last_toggle_time >= 500:
                autowalk = not autowalk
                last_toggle_time = current_time
                print("Toggled autowalk:", autowalk)
        # print(event)
            
    screen.fill(WHITE)
    x, y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    pygame.draw.line(screen, (175, 222, 209), (target.x, target.y), (Body.x, Body.y), 5)
    Body.draw(screen)
    Ankle1.draw(screen)
    Ankle2.draw(screen)
    Foot1.draw(screen)
    Foot2.draw(screen)
    target.draw(screen)
    
    # print("Distance:", getDistance(Body, Ankle1))
    if not autowalk:
        normalPhysWalk()
        # print("Normal walking")
    elif autowalk:
        normalPhysWalk()
        autoWalk(target)
        # print("Auto walking")
    pygame.draw.line(screen, (0,0,0), (Foot1.x, Foot1.y), (Ankle1.x, Ankle1.y), 3)
    pygame.draw.line(screen, (0,0,0), (Foot2.x, Foot2.y), (Ankle2.x, Ankle2.y), 3)
    pygame.draw.line(screen, (0,0,0), (Foot1.x, Foot1.y), (Body.x, Body.y), 3)
    pygame.draw.line(screen, (0,0,0), (Foot2.x, Foot2.y), (Body.x, Body.y), 3)
    
    # pygame.draw.line(screen, BLUE, (Ankle1.x, Ankle1.y), (Ankle2.x, Ankle2.y), 3)    
    pygame.display.flip()
    clock.tick(60)
    # print(Anklemid.x,Anklemid.y)

pygame.quit()
